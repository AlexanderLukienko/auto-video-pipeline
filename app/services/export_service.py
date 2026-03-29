import shutil
import time
from pathlib import Path
from typing import Optional, List

from app.config.paths import CAPCUT_EXPORT_DIR, DONE_DIR, ARCHIVE_DIR
from app.models.job import Job


class ExportStateError(Exception):
    pass


def list_recent_capcut_files() -> List[Path]:
    files = [p for p in CAPCUT_EXPORT_DIR.iterdir() if p.is_file()]
    files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return files


def find_exported_file_for_job(job: Job) -> Optional[Path]:
    """
    Ищем файл, который начинается с имени job.
    Например:
    job.original_name = '6.mp4'
    export name in CapCut could be '6.mov'
    или '6.mp4.mov'
    """

    original_stem = Path(job.original_name).stem  # '6'

    candidates = [
        p for p in CAPCUT_EXPORT_DIR.iterdir()
        if p.is_file() and p.name.startswith(original_stem)
    ]

    if not candidates:
        return None

    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0]


def is_file_stable(file_path: Path, stable_wait_seconds: float = 2.0) -> bool:
    """
    Проверяем, что файл перестал расти.
    """
    if not file_path.exists() or not file_path.is_file():
        return False

    size_1 = file_path.stat().st_size
    time.sleep(stable_wait_seconds)

    if not file_path.exists():
        return False

    size_2 = file_path.stat().st_size
    return size_1 == size_2 and size_2 > 0


def wait_for_exported_file(
    job: Job,
    timeout_seconds: float = 300.0,
    poll_interval: float = 2.0,
    stable_wait_seconds: float = 2.0,
) -> Path:
    """
    Ждет, пока экспортированный файл:
    1. появится в папке CapCut
    2. перестанет расти

    timeout_seconds=300 => ждем до 5 минут
    """
    deadline = time.time() + timeout_seconds

    while time.time() < deadline:
        candidate = find_exported_file_for_job(job)

        if candidate is not None:
            print(f"DEBUG: found export candidate: {candidate.name}")

            if is_file_stable(candidate, stable_wait_seconds=stable_wait_seconds):
                print(f"DEBUG: export file is stable: {candidate.name}")
                return candidate

            print(f"DEBUG: file exists but is still growing: {candidate.name}")
        else:
            print("DEBUG: export file not found yet")

        time.sleep(poll_interval)

    recent_files = [p.name for p in list_recent_capcut_files()[:10]]
    raise ExportStateError(
        f"Файл экспорта не появился или не стабилизировался за "
        f"{timeout_seconds} сек для job '{job.original_name}'. "
        f"Последние файлы в CapCut: {recent_files}"
    )


def move_export_to_done(exported_file: Path) -> Path:
    destination = DONE_DIR / exported_file.name
    shutil.move(str(exported_file), str(destination))
    return destination


def archive_original_work_file(job: Job) -> Path:
    if not job.work_path.exists():
        raise ExportStateError(
            f"Исходный рабочий файл не найден: {job.work_path}"
        )

    destination = ARCHIVE_DIR / job.original_name
    shutil.move(str(job.work_path), str(destination))
    return destination


def finalize_exported_job(job: Job) -> tuple[Path, Path]:
    """
    1. Ждем экспортированный файл
    2. Перемещаем его в Готовые видео
    3. Исходник из В работе переносим в Архив
    """
    exported_file = wait_for_exported_file(job)
    done_file = move_export_to_done(exported_file)
    archived_original = archive_original_work_file(job)

    return done_file, archived_original