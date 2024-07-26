import pyautogui
import pygetwindow as gw
import time
import keyboard

def press_enter():
    pyautogui.press('enter')

while True:
    error_window = gw.getWindowsWithTitle('Erro')
    if error_window:
        press_enter()

    pergunta_window = gw.getWindowsWithTitle('Pergunta')
    if pergunta_window:
        press_enter()

    infor_window = gw.getWindowsWithTitle('Informação')
    if infor_window:
        press_enter()


    if keyboard.is_pressed('esc'):
        break


    time.sleep(1)