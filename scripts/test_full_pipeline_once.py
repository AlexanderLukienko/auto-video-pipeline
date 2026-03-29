import time
from app.services.export_service import finalize_exported_job
from pathlib import Path

from app.services.file_service import (
    get_next_video,
    move_to_work,
    get_current_work_file,
    ensure_work_dir_is_ready_for_new_job,
)
from app.utils.video_checks import is_file_ready
from app.services.capcut.workflow import start_new_project
from app.services.capcut.actions import open_import_window, confirm_import_file
from app.services.capcut.actions import add_video_to_timeline
from app.services.capcut.actions import open_enhance_panel, scroll_enhance_panel
from app.services.capcut.actions import (
    enable_enhance_quality,
    generate_subtitles,
)

from app.services.capcut.actions import (
    open_export_window,
    set_export_filename,
    confirm_export,
    wait_for_export_to_finish,
    close_export_popup,
    close_project,
)


def main():
    print("=== START FULL PIPELINE TEST ===")

    # 1. Проверяем, что папка 'В работе' готова
    ensure_work_dir_is_ready_for_new_job()
    print("✅ Папка 'В работе' пустая, можно начинать новый job")

    # 2. Берем следующее видео из 'На обработку'
    video = get_next_video()
    if not video:
        print("❌ В папке 'На обработку' нет видео")
        return

    print(f"🎥 Найдено первое видео для обработки: {video.name}")

    # 3. Проверяем, что файл полностью докопировался
    if not is_file_ready(video):
        print(f"⏳ Файл еще копируется: {video.name}")
        return

    # 4. Переносим в 'В работе'
    job = move_to_work(video)
    print(f"✅ Перенесено в 'В работе': {job.work_path.name}")

    current_work_file = get_current_work_file()
    if current_work_file is None:
        print("❌ Ошибка: после переноса файл не найден в 'В работе'")
        return

    print(f"📂 Текущий рабочий файл: {current_work_file.name}")

    # 5. Открываем CapCut и создаем проект
    start_new_project()
    print("✅ Новый проект в CapCut открыт")

    # 6. Открываем окно импорта
    time.sleep(1.5)
    open_import_window()
    print("✅ Окно импорта открыто")

    # 7. Импортируем файл
    time.sleep(1.5)
    confirm_import_file()
    print("✅ Файл импортирован в CapCut")

    add_video_to_timeline()
    print("✅ Видео добавлено на timeline")

    open_enhance_panel()
    scroll_enhance_panel()

    print("✅ Enhance panel opened and scrolled")

    enable_enhance_quality()
    generate_subtitles()

    print("✅ Enhance + subtitles done")

    from app.services.capcut.actions import (
    select_video_on_timeline,
    apply_retouch,
    adjust_audio,
)

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

    print("✅ Export flow completed")
    
    done_file, archived_file = finalize_exported_job(job)

    print(f"✅ Export moved to done: {done_file.name}")
    print(f"✅ Original moved to archive: {archived_file.name}")

    print("=== TEST FINISHED SUCCESSFULLY ===")


if __name__ == "__main__":
    main()