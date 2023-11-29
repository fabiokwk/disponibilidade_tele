import pyautogui as py
import time
from function import verificar_tela
import subprocess
import openpyxl
import pyperclip
from datetime import datetime
import os
#variaveis auxiliares
tempo_limite_espera = 10
prog = """${SSN},SIGNAL,${TRY},${COUNT}
${SSN},VED,${TRY},${COUNT}
${SSN},TFS,${TRY},${COUNT}"""

#entrando na tela de listagem em si
def main():

    localiza('IRIS_IMAGENS/Listagem_telemetria.png', 0.8)
    py.click()
    localiza('IRIS_IMAGENS/Tela_listagem.png', 0.8)
    maximiza()
    localiza('IRIS_IMAGENS/inserir_min.png', 0.9)
    py.click(py.moveRel(0,10))
    py.write(teles)
    localiza('IRIS_IMAGENS/Lupa.png', 0.9)
    py.click()
    time.sleep(1.3)
    py.click(py.moveRel(0,82))
    py.hotkey('ctrl','a')
    py.rightClick()
    py.moveRel(5,10)
    py.click()
    selecionar_todas_as_teles()
    escrever_prog(prog)


def localiza(DIRETORIO, precisao):
    inicio_tempo = time.time()
    while not verificar_tela(DIRETORIO, precisao):
        decorrido = time.time() - inicio_tempo
        if  decorrido > tempo_limite_espera:
            print('Tempo limite atingido')
            inicio_tempo = time.time()
            exit;

with open('ucs_com_telemetrias_sem_disponibilidade','r') as arquivo:
    pre_lista = []
    for linha in arquivo:
        
        pre_lista.append(linha)
        pre_lista.append(';')
        telemetrias = ''.join([item.strip() for item in pre_lista])
        teles = telemetrias.rstrip(';')
    
def maximiza():
    localiza('IRIS_IMAGENS/MAx.png', 0.8)
    py.moveRel(30,-42)
    py.click()
    
def ver_mensagens():
    localiza('IRIS_IMAGENS/ver_mensagens.png', 0.8)
    py.moveRel(335,-267)
    py.click()
    localiza('IRIS_IMAGENS/hora.png', 0.8)
    py.click()
    localiza('IRIS_IMAGENS/chips.png', 0.8)
    py.click()
    localiza('IRIS_IMAGENS/teles.png', 0.8)
    py.click()
    py.hotkey('ctrl','a')

def maximiza_ver_mensagens():
    localiza('IRIS_IMAGENS/ver_mensagens.png', 0.8)
    py.moveRel(335,-267)
    py.click()
def escrever_prog(prog):#escreve o programa desejado no campo de comandos
    localiza('IRIS_IMAGENS/area_escrita_comandos.PNG', 0.8)
    # py.moveRel(335,-267)
    py.moveTo('IRIS_IMAGENS/area_escrita_comandos.PNG')
    py.click()
    py.write(prog)

def comando(Comandos):
    py.moveRel(150,0)
    py.click()
    py.hotkey('ctrl','a')
    py.write(Comandos)
    localiza('IRIS_IMAGENS/enviar.png', 0.9)
    py.click()

def selecionar_todas_as_teles():#seleciona todas as teles dentro do 'ver mensagens' antes de escrever o comando
    maximiza_ver_mensagens()
    localiza('IRIS_IMAGENS/selecionar_todas_as_teles.png', 0.9)
    py.click()

def confirma_envio_comandos():#confirma envio dos comandos
    localiza('IRIS_IMAGENS/enviar.png', 0.9)
    py.click()

def cria_xlsx():

    py.doubleClick(400,200)
    py.hotkey('ctrl','a')
    py.hotkey('ctrl','c')
    # Aguarde um breve momento para que a operação de copiar seja concluída
    time.sleep(1)  # Um segundo deve ser suficiente, mas ajuste conforme necessário
    # Lista dos dados extraídos está armazenada como uma string grande, com base no seu uso anterior
    dados_extraidos = pyperclip.paste()
    # Agora vamos criar um novo Workbook
    wb = openpyxl.Workbook()
    ws = wb.active
    # Dividindo o texto copiado em linhas e colunas
    linhas = dados_extraidos.strip().split('\n')  # separar cada linha pelo '\n'
    for i, linha in enumerate(linhas):
        # Dividindo cada linha em células baseadas na vírgula
        celulas = linha.split(',')  # separar cada célula pela vírgula
        for j, celula in enumerate(celulas):
            # Escrever cada célula na planilha
            ws.cell(row=i+1, column=j+1, value=celula.strip())  # Adiciona os dados nas células

    # Salvar o arquivo no mesmo diretório onde o script está sendo executado
    data_hoje = datetime.now()
    diretorio = r"C:\Users\L805678\Documents\Python\Pycis\Dados_iris_telemetria"
    # Formate a data no formato que você deseja no nome do arquivo (por exemplo, '2023-11-07')
    data_formatada = data_hoje.strftime('%d_%m_%Y-%H-%M')

    caminho_completo = os.path.join(diretorio, f'dados_exportados_{data_formatada}.xlsx')


    wb.save(caminho_completo)

if __name__ == '__main__':
    main()