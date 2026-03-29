import subprocess
import time


CAPCUT_APP_NAME = "CapCut"


class CapCutLaunchError(Exception):
    pass


def launch_capcut() -> None:
    """
    Запускает CapCut через macOS open command.
    """
    try:
        subprocess.run(
            ["open", "-a", CAPCUT_APP_NAME],
            check=True,
        )
    except subprocess.CalledProcessError as error:
        raise CapCutLaunchError(
            f"Не удалось запустить {CAPCUT_APP_NAME}"
        ) from error


def activate_capcut() -> None:
    """
    Делает CapCut активным приложением через AppleScript.
    """
    script = f'''
    tell application "{CAPCUT_APP_NAME}"
        activate
    end tell
    '''

    try:
        subprocess.run(
            ["osascript", "-e", script],
            check=True,
        )
    except subprocess.CalledProcessError as error:
        raise CapCutLaunchError(
            f"Не удалось активировать {CAPCUT_APP_NAME}"
        ) from error


def ensure_capcut_started(startup_wait_seconds: float = 3.0) -> None:
    """
    Минимальный launcher workflow:
    1. Запустить CapCut
    2. Подождать запуск
    3. Активировать окно
    4. Еще немного подождать для стабилизации
    """
    launch_capcut()
    time.sleep(startup_wait_seconds)
    activate_capcut()
    time.sleep(1.5)