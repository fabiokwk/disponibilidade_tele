import pyautogui as py
from time import sleep
import pyperclip
import keyboard
import datetime
import os
import sys
velocidade = 0.7 # type: ignore
stop_thread = False 

#definir velocidade de processamento
def speed(valor):
    global velocidade
    velocidade = valor
#funçao de para o algoritimo
def stop_alterar():
    global stop_thread
    stop_thread = not stop_thread
    sys.exit()
#funçao de verificar a tela e mover o mouse para seu centro
def verificar_tela(imagem, precisao):
    sleep(velocidade) # type: ignore
    tela_encontrada = py.locateOnScreen(imagem, confidence=precisao)
    py.moveTo(tela_encontrada)
    if tela_encontrada is not None and not stop_thread:
        nome_imagem = os.path.basename(imagem)
        print(f"A tela {nome_imagem} foi encontrada.")
        sleep(velocidade) # type: ignore
        return True
    else:
        if not stop_thread:
            nome_imagem = os.path.basename(imagem)
            print(f"A tela não foi encontrada. {nome_imagem}")
            return False
        else:
            sys.exit()
#funçao de eliminar popup
def popup(popup):
    print('inicio handle pop up')
    popup_position = py.locateOnScreen(popup,confidence=0.5)# Procurar a imagem do pop-up apenas na região de busca definida    
    py.moveTo(popup_position)
    if popup_position is not None and not stop_thread:#se há pop up
        print('há pop up')
        py.click(py.moveRel(-235,-47))
        py.click(py.moveRel(0,+59))
        py.click(py.moveRel(0,+59))
        py.moveTo(popup_position)
        py.click(py.moveRel(+229,+178))
    else:
        if not stop_thread:
            print('NÃO há pop up')
        else:
            sys.exit()