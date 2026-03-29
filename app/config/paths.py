from pathlib import Path

BASE_DIR = Path.home() / "Desktop" / "Автоматизация"

INPUT_DIR = BASE_DIR / "На обработку"
WORK_DIR = BASE_DIR / "В работе"
DONE_DIR = BASE_DIR / "Готовые видео"
ERROR_DIR = BASE_DIR / "Ошибка"
ARCHIVE_DIR = BASE_DIR / "Архив"
CAPCUT_EXPORT_DIR = Path.home() / "Movies" / "CapCut"

ALL_DIRS = [
    INPUT_DIR,
    WORK_DIR,
    DONE_DIR,
    ERROR_DIR,
    ARCHIVE_DIR,
]