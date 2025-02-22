import time
import pygetwindow as gw
import pyautogui

def list_windows():
    """
    Returns a list of titles of currently open windows.
    """
    windows = gw.getAllTitles()
    return [title for title in windows if title.strip() != '']

def capture_window(window_title):
    """
    Captures a screenshot of the window with the given title.
    
    Args:
        window_title (str): The title of the target window.
    
    Returns:
        PIL.Image: A screenshot image of the selected window.
    
    Raises:
        ValueError: If no window is found with the given title.
    """
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        raise ValueError("Window not found.")
    win = windows[0]
    # Bring the window to the front
    win.activate()
    time.sleep(0.5)  # Allow time for the window to become active
    left, top, width, height = win.left, win.top, win.width, win.height
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot
