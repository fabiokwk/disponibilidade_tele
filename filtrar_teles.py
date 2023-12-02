import pandas as pd
from time import sleep
import pyautogui as py
import webbrowser

def remover_do_hemera(remover_do_hemera_formatar):
    qtd_itens = len(remover_do_hemera_formatar)
    for i in range(qtd_itens):
        py.press('winleft', presses=2, interval=1)


caminho_do_arquivo = "textos_tabelas/status_teles.xlsx"# caminho do arquivo original
dados_geral = pd.read_excel(caminho_do_arquivo, header=None)# variável com conteúdo do arquivo original
lista_desconectadas = dados_geral[~dados_geral.iloc[:,14].str.lower().str.startswith(('sucata', 'reserva'), na=False)][dados_geral.iloc[:,1] == 0]#subdataset com teles desconectadas
lista_desconectadas = lista_desconectadas.iloc[:,[12,14]]
lista_conectadas = dados_geral.iloc[:,12][dados_geral.iloc[:,1] == 1]#subdataset com teles conectadas
lista_remover_hemera = dados_geral[dados_geral.iloc[:,14].str.lower().str.startswith(('sucata', 'reserva'), na=False)]
lista_remover_hemera = lista_remover_hemera.iloc[:,[12,14]]

print(dados_geral.shape)
print(lista_conectadas.shape)
print(lista_desconectadas.shape)

conectadas_formatar = []
for linha in lista_conectadas:
    conectadas_formatar.append(str(linha))

conectadas = ';'.join(conectadas_formatar)

desconectadas_formatar = []
for linha in lista_desconectadas.iloc[:,0]:
    desconectadas_formatar.append(str(linha))

desconectadas_avaliar = ';'.join(desconectadas_formatar)

remover_do_hemera_formatar = []
for linha in lista_remover_hemera.iloc[:,0]:
    remover_do_hemera_formatar.append(str(linha))

desconectadas_remover = ';'.join(remover_do_hemera_formatar)

print('--------------------------------------')
print('CONECTADAS')
print(conectadas)
print('--------------------------------------')
print('DESCONECTADAS')
print(desconectadas_avaliar)
print('--------------------------------------')
print('REMOVER DO HEMERA')
print(desconectadas_remover)
print('--------------------------------------')
print('LISTA_REMOVER_HEMERA')
print(lista_remover_hemera)
print('--------------------------------------')
print('REMOVER_DO_HEMERA_FORMATAR')
print(remover_do_hemera_formatar)


