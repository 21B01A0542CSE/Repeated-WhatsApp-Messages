import pyautogui
import time 
time.sleep(3)
for i in range(2):
    pyautogui.typewrite("hello")
    pyautogui.press("enter")
