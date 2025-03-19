import pyautogui
import time

pyautogui.PAUSE = 0.3

#pegar posi~ções mouse e da tela
print(pyautogui.position())
print(pyautogui.size())

#função do mouse
time.sleep(5)
#pyautogui.click(x=2567, y=266)

pyautogui.moveTo(x=2532, y=112, duration=1)
pyautogui.click(x=3201, y=335, interval=0.25)
pyautogui.scroll(-880)

