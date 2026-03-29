from app.services.capcut.launcher import ensure_capcut_started
from app.services.capcut.window_manager import prepare_capcut_window


def main():
    ensure_capcut_started()
    prepare_capcut_window()

    print("✅ Окно подготовлено")


if __name__ == "__main__":
    main()