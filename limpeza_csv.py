import pandas as pd
import datetime

caminho_do_arquivo = "relatorio_de_disponibilidade.xlsx"# caminho do arquivo original
dados_geral = pd.read_excel(caminho_do_arquivo)# variável com conteúdo do arquivo original
dados = dados_geral.iloc[:, [0, 1, 2, 3, 6]][dados_geral['Disponibilidade'] == 0]#subdataset do arquivo original
data_hora_atual = datetime.datetime.now()#data e hora
data_formatada = data_hora_atual.strftime('%Y-%m-%d %H:%M:%S')#data e hora formatada
print(dados_geral.shape)#shape arquivo original
print(dados.shape)#shape arquivo subdataset
dados.to_csv('ucs_com_telemetrias_sem_disponibilidade', index=False, header=False)#escreve o subdataset em um arquivo txt

