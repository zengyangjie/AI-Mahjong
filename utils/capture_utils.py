import pygetwindow as gw
import pyautogui

def capture_window(window_title="欢乐麻将全集"):
    """
    捕获指定窗口的截图。

    参数:
        window_title (str): 窗口标题，默认值为 "欢乐麻将全集"。

    返回:
        PIL.Image 或 None: 返回截图的 PIL.Image 对象，如果窗口未找到则返回 None。
    """
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        window = windows[0]
        left, top, width, height = window.left, window.top, window.width, window.height
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        return screenshot
    else:
        print(f"窗口 '{window_title}' 未找到。")
        return None
