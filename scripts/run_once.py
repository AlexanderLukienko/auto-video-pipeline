from app.services.file_service import get_next_video, move_to_work
from app.utils.video_checks import is_file_ready


def main():
    video = get_next_video()

    if not video:
        print("❌ Нет видео в папке 'На обработку'")
        return

    print(f"🎥 Найден файл: {video.name}")

    if not is_file_ready(video):
        print("⏳ Файл еще копируется, пропускаем")
        return

    job = move_to_work(video)
    print(f"✅ Перемещен в работу: {job.work_path.name}")
    print(job)


if __name__ == "__main__":
    main()