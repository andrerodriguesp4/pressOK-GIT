import pyautogui
import pygetwindow as gw
import time
import keyboard

def press_enter():
    pyautogui.press('enter')

while True:
    error_window = gw.getWindowsWithTitle('Error')
    if error_window:
        press_enter()

    if keyboard.is_pressed('esc'):
        break


    time.sleep(1)