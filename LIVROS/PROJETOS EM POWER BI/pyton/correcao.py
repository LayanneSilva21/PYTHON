import pyautogui as 
import time

pyautogui.PAUSE = 5.3

def abrir_nav():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(2)  # Aguarda o navegador abrir
    posicao = pyautogui.locateOnScreen("RDA.png", confidence=0.8)
    if posicao:
        pyautogui.doubleClick(posicao)
    try:
        maxim = pyautogui.locateOnScreen("max.png")
        if maxim:
            pyautogui.click(maxim)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

abrir_nav()
