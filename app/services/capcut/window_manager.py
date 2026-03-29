import subprocess
import time


CAPCUT_APP_NAME = "CapCut"


class CapCutWindowError(Exception):
    pass


def run_applescript(script: str) -> str:
    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise CapCutWindowError(result.stderr.strip() or "AppleScript command failed")

    return result.stdout.strip()


def activate_capcut() -> None:
    script = f'''
    tell application "{CAPCUT_APP_NAME}"
        activate
    end tell
    '''
    run_applescript(script)


def get_window_count() -> int:
    script = f'''
    tell application "System Events"
        tell application process "{CAPCUT_APP_NAME}"
            return count of windows
        end tell
    end tell
    '''
    output = run_applescript(script)
    return int(output)


def try_zoom_capcut_window() -> bool:
    script = f'''
    tell application "System Events"
        tell application process "{CAPCUT_APP_NAME}"
            set frontmost to true
            if (count of windows) is 0 then error "No windows found for CapCut"

            tell window 1
                perform action "AXZoom"
            end tell
        end tell
    end tell
    '''

    try:
        run_applescript(script)
        return True
    except CapCutWindowError:
        return False


def prepare_capcut_window() -> None:
    activate_capcut()
    time.sleep(1)

    window_count = get_window_count()
    if window_count == 0:
        raise CapCutWindowError("CapCut window was not found")

    zoom_success = try_zoom_capcut_window()

    if zoom_success:
        print("✅ CapCut window zoomed")
    else:
        print("⚠️ AXZoom недоступен, продолжаем без zoom")

    time.sleep(1.0)