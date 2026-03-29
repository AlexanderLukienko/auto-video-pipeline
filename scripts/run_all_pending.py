import time

from app.services.pipeline_service import process_one_pending_video, PipelineError
from app.services.file_service import FileStateError
from app.services.export_service import ExportStateError


def main():
    print("=== START BATCH PROCESSING ===")

    processed_count = 0

    while True:
        try:
            processed = process_one_pending_video()

            if not processed:
                break

            processed_count += 1
            print(f"✅ Обработано видео: {processed_count}")

            # маленькая пауза между job, чтобы UI успел успокоиться
            time.sleep(2)

        except (PipelineError, FileStateError, ExportStateError) as error:
            print(f"❌ Ошибка пайплайна: {error}")
            break

        except Exception as error:
            print(f"❌ Неожиданная ошибка: {error}")
            break

    print(f"=== BATCH FINISHED. Всего обработано: {processed_count} ===")


if __name__ == "__main__":
    main()