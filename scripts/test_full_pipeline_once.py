import time

from app.services.file_service import (
    get_next_video,
    move_to_work,
    get_current_work_file,
    ensure_work_dir_is_ready_for_new_job,
)
from app.utils.video_checks import is_file_ready
from app.services.capcut.workflow import start_new_project
from app.services.capcut.actions import open_import_window, confirm_import_file


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

    print("=== TEST FINISHED SUCCESSFULLY ===")


if __name__ == "__main__":
    main()