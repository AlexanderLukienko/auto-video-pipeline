import time
import pyautogui

from app.config.timings import (
    IMPORT_OPEN_DELAY,
    IMPORT_SELECTION_DELAY,
    IMPORT_CONFIRM_DELAY,
)

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

CREATE_PROJECT_X = 694
CREATE_PROJECT_Y = 148


def click_create_project() -> None:
    print("DEBUG: click Create project at (694, 148)")
    pyautogui.moveTo(CREATE_PROJECT_X, CREATE_PROJECT_Y, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(2.0)


def open_import_window() -> None:
    print("DEBUG: Cmd+I")
    pyautogui.hotkey("command", "i")
    time.sleep(IMPORT_OPEN_DELAY)


def confirm_import_file() -> None:
    print("DEBUG: Down")
    pyautogui.press("down")
    time.sleep(IMPORT_SELECTION_DELAY)

    print("DEBUG: Enter")
    pyautogui.press("enter")
    time.sleep(IMPORT_CONFIRM_DELAY)