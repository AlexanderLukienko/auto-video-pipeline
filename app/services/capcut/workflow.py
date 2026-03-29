import time

from app.services.capcut.actions import click_create_project
from app.services.capcut.launcher import ensure_capcut_started
from app.services.capcut.window_manager import prepare_capcut_window
from app.config.timings import CREATE_PROJECT_DELAY


class CapCutWorkflowError(Exception):
    pass


def start_new_project() -> None:
    ensure_capcut_started()
    prepare_capcut_window()

    print("Через 2 секунды будет клик по Create project...")
    time.sleep(CREATE_PROJECT_DELAY)

    click_create_project()
    print("✅ Клик по Create project выполнен")