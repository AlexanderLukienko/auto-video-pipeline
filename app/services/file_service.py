import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from app.config.paths import ARCHIVE_DIR, INPUT_DIR, WORK_DIR
from app.models.job import Job
from app.utils.video_checks import is_video_file


class FileStateError(Exception):
    pass


def get_next_video() -> Optional[Path]:
    files = [path for path in INPUT_DIR.iterdir() if is_video_file(path)]

    if not files:
        return None

    files.sort(key=lambda path: path.stat().st_mtime)
    return files[0]


def get_work_videos() -> List[Path]:
    files = [path for path in WORK_DIR.iterdir() if is_video_file(path)]
    files.sort(key=lambda path: path.stat().st_mtime)
    return files


def ensure_work_dir_is_ready_for_new_job() -> None:
    work_files = get_work_videos()

    if len(work_files) > 1:
        raise FileStateError(
            f"В папке 'В работе' больше одного файла: {len(work_files)}"
        )

    if len(work_files) == 1:
        raise FileStateError(
            f"В папке 'В работе' уже есть файл: {work_files[0].name}"
        )


def get_current_work_file() -> Optional[Path]:
    work_files = get_work_videos()

    if len(work_files) > 1:
        raise FileStateError(
            f"В папке 'В работе' больше одного файла: {len(work_files)}"
        )

    if len(work_files) == 0:
        return None

    return work_files[0]


def move_to_work(file_path: Path) -> Job:
    ensure_work_dir_is_ready_for_new_job()

    original_name = file_path.name
    job_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_name = f"{job_id}__{original_name}"
    work_path = WORK_DIR / new_name

    shutil.move(str(file_path), str(work_path))

    return Job(
        job_id=job_id,
        original_name=original_name,
        work_path=work_path,
    )


def archive_file(file_path: Path) -> Path:
    archive_path = ARCHIVE_DIR / file_path.name
    shutil.move(str(file_path), str(archive_path))
    return archive_path