from app.services.capcut.workflow import start_new_project
from app.services.capcut.actions import open_import_window, confirm_import_file

import time


def main():
    start_new_project()

    print("Открываем импорт...")
    time.sleep(2)
    open_import_window()

    print("Импортируем файл...")
    time.sleep(2)
    confirm_import_file()

    print("✅ Файл отправлен в CapCut")


if __name__ == "__main__":
    main()