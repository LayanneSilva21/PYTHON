import pyautogui
import time

pyautogui.PAUSE = 1.3

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

    time.sleep(1)

def abrir_site():
    time.sleep(2)  # Aguarda o navegador carregar
    pyautogui.write("cpag.rdamasio.com.br")
    pyautogui.press("enter")
    time.sleep(3)  # Aguarda o site carregar
    pyautogui.write("laiane.pereira")
    pyautogui.press("tab")
    pyautogui.write("813147L@Y")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

def abrir_tela():
    time.sleep(3)  # Aguarda a página carregar
    estrela = pyautogui.locateOnScreen("estrela.png")
    pyautogui.moveTo(estrela)
    pyautogui.click(button="left")
    cham = pyautogui.locateOnScreen("cham.png")
    pyautogui.moveTo(cham)
    pyautogui.click(button="left")


# Executa as funções
abrir_nav()
abrir_site()
abrir_tela()
