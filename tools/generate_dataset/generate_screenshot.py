import win32gui
import time
import threading
from pynput import keyboard
from utils.capture_utils import capture_window
import os

# 全局变量控制截屏状态
is_running = False
is_stopped = threading.Event()

# 创建 raw_screenshot 文件夹（如果不存在）
def create_screenshot_folder():
    folder_path = "raw_screenshot"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print("文件夹 'raw_screenshot' 已创建。")
    else:
        print("文件夹 'raw_screenshot' 已存在。")
    return folder_path

def bring_window_to_front(window_title="欢乐麻将全集"):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)  # 将窗口置于前面
        time.sleep(1)  # 等待窗口更新
        return True
    else:
        print(f"窗口 '{window_title}' 未找到。")
        return False


def screenshot_loop(window_title="欢乐麻将全集"):
    global is_running
    screenshot_folder = create_screenshot_folder()  # 创建截图文件夹
    while True:
        if is_running:
            image = capture_window(window_title)
            if image:
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                image_path = os.path.join(screenshot_folder, f"screenshot_{timestamp}.png")
                image.save(image_path)
                print(f"截图保存为 {image_path}")
            else:
                print("截图失败。")
        else:
            print("截图已暂停，线程等待中...")
            is_stopped.wait()  # 等待被唤醒
        time.sleep(5)  # 每隔 5 秒截图一次

def on_key_press(key):
    global is_running
    try:
        if key == keyboard.Key.home:  # Home 键启动截屏
            if not is_running:
                print("启动截图功能。")
                is_running = True
                is_stopped.set()  # 唤醒截图线程
        elif key == keyboard.Key.end:  # End 键暂停截屏
            if is_running:
                print("暂停截图功能。")
                is_running = False
                is_stopped.clear()  # 暂停截图线程
    except Exception as e:
        print(f"监听按键时发生错误：{e}")

def main():
    window_title = "欢乐麻将全集"

    # 确保窗口置于前面
    if bring_window_to_front(window_title):
        print("窗口已成功置于前面。")
    else:
        print("窗口操作失败。")

    # 创建截图线程
    screenshot_thread = threading.Thread(target=screenshot_loop, args=(window_title,), daemon=True)
    screenshot_thread.start()

    # 监听键盘输入
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
