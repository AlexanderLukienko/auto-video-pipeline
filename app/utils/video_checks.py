import time
from pathlib import Path

VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".avi", ".m4v"}


def is_video_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in VIDEO_EXTENSIONS


def is_file_ready(path: Path, wait_seconds: int = 2) -> bool:
    size_1 = path.stat().st_size
    time.sleep(wait_seconds)
    size_2 = path.stat().st_size
    return size_1 == size_2 and size_2 > 0