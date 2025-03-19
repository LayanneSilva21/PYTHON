import pyautogui
import time

pyautogui.PAUSE = 5.3

def abrir_navegador():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    pyautogui.moveTo(x=944, y=625)
    pyautogui.doubleClick()
    time.sleep(1)

def navegar_para_site():
    pyautogui.write("hashtagtreinamentos.com")
    pyautogui.press("enter")
    time.sleep(2)

def acessar_curso():
    posicao_curso = pyautogui.locateCenterOnScreen("CURSOS.png")
    posicao_html = pyautogui.locateCenterOnScreen("HTML.png")
    if posicao_curso and posicao_html:
        pyautogui.doubleClick(posicao_curso)
        pyautogui.moveTo(x=635, y=146)
        pyautogui.moveTo(x=1189, y=371)
    else:
        print("Elementos não encontrados na tela.")

# Executando as funções
abrir_navegador()
navegar_para_site()
acessar_curso()
