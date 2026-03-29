from app.services.capcut.launcher import ensure_capcut_started
from app.services.capcut.window_manager import prepare_capcut_window
from app.services.capcut.workflow import start_new_project
from app.services.capcut.actions import open_import_window


def main():
    start_new_project()

    print("Через 2 секунды откроется импорт...")
    import time
    time.sleep(2)

    open_import_window()

    print("✅ Импорт открыт")


if __name__ == "__main__":
    main()