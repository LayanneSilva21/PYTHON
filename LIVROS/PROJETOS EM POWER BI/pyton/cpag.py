import pyautogui
import time

pyautogui.PAUSE = 0.3

# Pegar posições do mouse e da tela
print(pyautogui.position())
print(pyautogui.size())

# Função do mouse
time.sleep(5)
# pyautogui.click(x=2567, y=266)

pyautogui.click(x=2885, y=597, duration=1, interval=0.25)
# pyautogui.click(x=2876, y=601, clicks=2, interval=0.25)

# Mover o mouse para a posição desejada antes de rolar
pyautogui.moveTo(x=2653, y=176)
pyautogui.moveTo(x=2668, y=209)
pyautogui.click(button='left', clicks=2, interval=0.25)
pyautogui.scroll(-880)

#funções de teclado


