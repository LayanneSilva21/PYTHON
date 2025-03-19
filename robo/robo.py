import time
from os import startfile, sep
from subprocess import call

from pyautogui import write, press, hotkey, typewrite, moveTo, click
from pyscreeze import locateOnScreen
import PIL

cnpjs= ['21.456.428/0001','20.908.439/0001', '29.262.605/0001', '27.293.198/0001', '27.933.716/0001', '35.199.545/0001']

call('taskkill /f /IM Menu.exe')
hotkey('win', 'd')
path = f'C:{sep}C5Client{sep}Pessoa{sep}Pessoa.exe'
startfile(path)
time.sleep(3)
write('laiane.silva')
press('tab')
write('81314752')
press('tab')
press('enter')
time.sleep(5)
hotkey('ctrl', 'p')
press('tab', presses=32)

for cnpj in cnpjs:
        print(cnpj)
        time.sleep(5)
        typewrite(cnpj)
        press('tab')
        press('enter')
        press('F8')
        time.sleep(8)
        moveTo(locateOnScreen('contatos.png'))
        click()
        time.sleep(3)
        press('F10')
        press('F2')
        press('tab', presses=32)

print('Processo Concluido')
