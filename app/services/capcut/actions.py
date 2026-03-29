import time
import pyautogui
import pyperclip

from app.config.timings import (
    IMPORT_OPEN_DELAY,
    IMPORT_SELECTION_DELAY,
    IMPORT_CONFIRM_DELAY,
    TIMELINE_IMPORT_WAIT,
    TIMELINE_CLICK_DELAY,
    ENHANCE_CLICK_DELAY,
    SUBTITLES_CLICK_DELAY,
    RETOUCH_DELAY,
    AUDIO_DELAY,
    EXPORT_WINDOW_DELAY,
    EXPORT_NAME_FIELD_DELAY,
    EXPORT_START_DELAY,
    EXPORT_FINISH_WAIT,
    EXPORT_POPUP_DELAY,
    PROJECT_CLOSE_DELAY,
)

from app.config.coords import (
    ENHANCE_BUTTON,
    SUBTITLES_STEP_1,
    SUBTITLES_STEP_2,
    SUBTITLES_STEP_3,
    SUBTITLES_STEP_4,
    SELECT_VIDEO,
    RETOUCH_TAB,
    RETOUCH_ENABLE,
    AUDIO_TAB,
    AUDIO_VOLUME,
    EXPORT_BUTTON,
    EXPORT_NAME_FIELD,
    EXPORT_CONFIRM,
    EXPORT_POPUP_CLOSE,
    CLOSE_PROJECT,
)

from app.config.coords import ENHANCE_PANEL


pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

CREATE_PROJECT_X = 694
CREATE_PROJECT_Y = 148

IMPORT_BUTTON_X = 287
IMPORT_BUTTON_Y = 210


def click_create_project() -> None:
    print("DEBUG: click Create project at (694, 148)")
    pyautogui.moveTo(CREATE_PROJECT_X, CREATE_PROJECT_Y, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(3.5)


def open_import_window() -> None:
    print(f"DEBUG: click Import button at ({IMPORT_BUTTON_X}, {IMPORT_BUTTON_Y})")
    pyautogui.moveTo(IMPORT_BUTTON_X, IMPORT_BUTTON_Y, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(IMPORT_OPEN_DELAY)


def confirm_import_file() -> None:
    print("DEBUG: Down")
    pyautogui.press("down")
    time.sleep(IMPORT_SELECTION_DELAY)

    print("DEBUG: Enter")
    pyautogui.press("enter")
    time.sleep(IMPORT_CONFIRM_DELAY)

MEDIA_ITEM_X = 248
MEDIA_ITEM_Y = 243

def add_video_to_timeline() -> None:
    import pyautogui
    import time

    print("DEBUG: waiting for media import to finish...")
    time.sleep(TIMELINE_IMPORT_WAIT)

    print(f"DEBUG: click media item at ({MEDIA_ITEM_X}, {MEDIA_ITEM_Y})")
    pyautogui.moveTo(MEDIA_ITEM_X, MEDIA_ITEM_Y, duration=0.3)
    time.sleep(0.2)

    pyautogui.click()
    time.sleep(TIMELINE_CLICK_DELAY)    

from app.config.coords import ENHANCE_PANEL


def open_enhance_panel() -> None:
    import pyautogui
    import time

    print(f"DEBUG: open enhance panel at {ENHANCE_PANEL}")

    pyautogui.moveTo(*ENHANCE_PANEL, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()

    time.sleep(1.5)

def scroll_enhance_panel() -> None:
    import pyautogui
    import time

    print("DEBUG: scrolling enhance panel")

    # важно: сначала навести курсор в область панели
    pyautogui.moveTo(1226, 202, duration=0.2)
    pyautogui.click()
    time.sleep(0.2)

    # скролл вниз (отрицательное значение)
    pyautogui.scroll(-600)
    pyautogui.scroll(-600)
    time.sleep(0.8)

from app.config.coords import (
    ENHANCE_BUTTON,
    SUBTITLES_STEP_1,
    SUBTITLES_STEP_2,
    SUBTITLES_STEP_3,
    SUBTITLES_STEP_4,
)

from app.config.timings import (
    ENHANCE_CLICK_DELAY,
    SUBTITLES_CLICK_DELAY,
)


def enable_enhance_quality() -> None:
    import pyautogui
    import time

    print(f"DEBUG: click enhance at {ENHANCE_BUTTON}")

    pyautogui.moveTo(*ENHANCE_BUTTON, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()

    time.sleep(ENHANCE_CLICK_DELAY)


def generate_subtitles() -> None:
    import pyautogui
    import time

    steps = [
        SUBTITLES_STEP_1,
        SUBTITLES_STEP_2,
        SUBTITLES_STEP_3,
        SUBTITLES_STEP_4,
    ]

    for i, (x, y) in enumerate(steps, start=1):
        print(f"DEBUG: subtitles step {i} at ({x}, {y})")

        pyautogui.moveTo(x, y, duration=0.3)
        time.sleep(0.2)
        pyautogui.click()

        time.sleep(SUBTITLES_CLICK_DELAY)

def select_video_on_timeline() -> None:
    import pyautogui
    import time

    print(f"DEBUG: select video at {SELECT_VIDEO}")

    pyautogui.moveTo(*SELECT_VIDEO, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()

    time.sleep(0.8)


def apply_retouch() -> None:
    import pyautogui
    import time

    print(f"DEBUG: open retouch tab at {RETOUCH_TAB}")

    pyautogui.moveTo(*RETOUCH_TAB, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()

    time.sleep(RETOUCH_DELAY)

    print(f"DEBUG: enable retouch at {RETOUCH_ENABLE}")

    pyautogui.moveTo(*RETOUCH_ENABLE, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()

    time.sleep(RETOUCH_DELAY)


def adjust_audio() -> None:
    import pyautogui
    import time

    print(f"DEBUG: open audio tab at {AUDIO_TAB}")

    pyautogui.moveTo(*AUDIO_TAB, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()

    time.sleep(AUDIO_DELAY)

    print(f"DEBUG: adjust volume at {AUDIO_VOLUME}")

    pyautogui.moveTo(*AUDIO_VOLUME, duration=0.3)
    time.sleep(0.2)

    # можно просто клик
    pyautogui.click()

    # или чуть "прокрутить" громкость (если это слайдер)
    # pyautogui.dragRel(50, 0, duration=0.2)

    time.sleep(AUDIO_DELAY)


def open_export_window() -> None:
    print(f"DEBUG: open export window at {EXPORT_BUTTON}")
    pyautogui.moveTo(*EXPORT_BUTTON, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(EXPORT_WINDOW_DELAY)


def set_export_filename(filename: str) -> None:
    import time
    import pyautogui
    import pyperclip

    print(f"DEBUG: set export filename: {filename}")

    # 1. Наводимся и кликаем в поле
    pyautogui.moveTo(*EXPORT_NAME_FIELD, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.5)

    # 2. На всякий случай еще раз кликаем
    pyautogui.click()
    time.sleep(0.3)

    # 3. Выделяем весь текст
    pyautogui.hotkey("command", "a")
    time.sleep(0.3)

    # 4. Удаляем выделенное
    pyautogui.press("backspace")
    time.sleep(0.4)

    # 5. Еще раз страхуемся: если вдруг не удалилось, повторим
    pyautogui.hotkey("command", "a")
    time.sleep(0.2)
    pyautogui.press("backspace")
    time.sleep(0.4)

    # 6. Вставляем новое имя
    pyperclip.copy(filename)
    pyautogui.hotkey("command", "v")
    time.sleep(0.6)


def confirm_export() -> None:
    print(f"DEBUG: confirm export at {EXPORT_CONFIRM}")
    pyautogui.moveTo(*EXPORT_CONFIRM, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(EXPORT_START_DELAY)


def wait_for_export_to_finish() -> None:
    print(f"DEBUG: waiting for export to finish: {EXPORT_FINISH_WAIT} sec")
    time.sleep(EXPORT_FINISH_WAIT)


def close_export_popup() -> None:
    print(f"DEBUG: close export popup at {EXPORT_POPUP_CLOSE}")
    pyautogui.moveTo(*EXPORT_POPUP_CLOSE, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(EXPORT_POPUP_DELAY)


def close_project() -> None:
    print(f"DEBUG: close project at {CLOSE_PROJECT}")
    pyautogui.moveTo(*CLOSE_PROJECT, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(PROJECT_CLOSE_DELAY)