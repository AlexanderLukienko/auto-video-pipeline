import time
from pathlib import Path

from app.services.file_service import (
    get_next_video,
    move_to_work,
    get_current_work_file,
    ensure_work_dir_is_ready_for_new_job,
)
from app.services.export_service import finalize_exported_job
from app.utils.video_checks import is_file_ready

from app.services.capcut.workflow import start_new_project
from app.services.capcut.actions import (
    open_import_window,
    confirm_import_file,
    add_video_to_timeline,
    open_enhance_panel,
    scroll_enhance_panel,
    enable_enhance_quality,
    generate_subtitles,
    select_video_on_timeline,
    apply_retouch,
    adjust_audio,
    open_export_window,
    set_export_filename,
    confirm_export,
    wait_for_export_to_finish,
    close_export_popup,
    close_project,
)


class PipelineError(Exception):
    pass


def process_one_pending_video() -> bool:
    """
    Обрабатывает одно видео из папки 'На обработку'.

    Returns:
        True  -> если видео было найдено и обработка запущена
        False -> если в папке 'На обработку' больше нет видео
    """
    print("=== START ONE VIDEO PIPELINE ===")

    ensure_work_dir_is_ready_for_new_job()
    print("✅ Папка 'В работе' пустая")

    video = get_next_video()
    if not video:
        print("ℹ️ В папке 'На обработку' больше нет видео")
        return False

    print(f"🎥 Найдено видео: {video.name}")

    if not is_file_ready(video):
        print(f"⏳ Файл еще копируется, пропускаем: {video.name}")
        return False

    job = move_to_work(video)
    print(f"✅ Перенесено в 'В работе': {job.work_path.name}")

    current_work_file = get_current_work_file()
    if current_work_file is None:
        raise PipelineError("После переноса файл не найден в 'В работе'")

    print(f"📂 Текущий рабочий файл: {current_work_file.name}")

    # CapCut pipeline
    start_new_project()
    print("✅ Новый проект в CapCut открыт")

    open_import_window()
    print("DEBUG: import window action sent")

    confirm_import_file()
    print("DEBUG: import file action sent")

    add_video_to_timeline()
    print("✅ Видео добавлено на timeline")

    open_enhance_panel()
    scroll_enhance_panel()
    print("✅ Enhance panel opened and scrolled")

    enable_enhance_quality()
    generate_subtitles()
    print("✅ Enhance + subtitles done")

    select_video_on_timeline()
    apply_retouch()
    adjust_audio()
    print("✅ Retouch + audio applied")

    export_filename = Path(job.original_name).stem

    open_export_window()
    set_export_filename(export_filename)
    confirm_export()
    wait_for_export_to_finish()
    close_export_popup()
    close_project()
    print("✅ Export UI flow completed")

    done_file, archived_file = finalize_exported_job(job)
    print(f"✅ Export moved to done: {done_file.name}")
    print(f"✅ Original moved to archive: {archived_file.name}")

    print("=== ONE VIDEO PIPELINE FINISHED ===")
    return True