import pyautogui
import time


pyautogui.PAUSE = 1


pyautogui.press("win")
pyautogui.write("bloco de notas")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write(
    "Ola esse é um exemplo de como entrar no Bloco de Notas e Digitar algo sem que você mexa no seu computador")
time.sleep(2)
pyautogui.hotkey("win", "1")
pyautogui.press("tab")
