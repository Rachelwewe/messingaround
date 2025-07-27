import pyautogui
import time

print("Move your mouse to a position. Press Ctrl+C to stop.\n")

try:
    while True:
        x, y = pyautogui.position()
        position_str = f"X: {x} Y: {y}"
        print(position_str, end='\r')  # overwrite line
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped.")
