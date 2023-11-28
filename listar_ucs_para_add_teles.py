'''Esse programa cria o arquivo lista_para_add_telemetria a partir do ucs_com_telemetrias_sem_disponibilidade'''
import re

def transformar_padrao(texto):
    padrao_regional = r'^(.{7})' #padrão para encontrar a regional
    padrao_uc = r'\b\d{8,}\b' #padrão para encontrar a UC

    correspondencia_regional = re.search(padrao_regional, texto)#search no texto para encontrar padrão_regional
    correspondencia_uc = re.search(padrao_uc, texto)#search no texto para encontrar padrão_uc

    if correspondencia_regional and correspondencia_uc:#verificar se há correspondência para continuar
        regional = correspondencia_regional.group(1)# Extrai os 7 primeiros caracteres
        numero_uc = correspondencia_uc.group()# Extrai o número da correspondência

        return f"{regional},{numero_uc}"# Retorna a string formatada
    else:#caso não haja correspondências
        return 'Sem dados compatíveis'

arquivo_entrada = 'ucs_com_telemetrias_sem_disponibilidade' # Nome do arquivo de entrada
arquivo_saida = 'lista_para_add_telemetria.txt'# Nome do arquivo de saídda

with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:# Abrir o arquivo de entrada para leitura e o arquivo de saída para escrita
    
    for linha in entrada:# Iterar sobre as linhas do arquivo de entrada
        
        linha_transformada = transformar_padrao(linha.strip())# Aplicar a função transformar_padrao a cada linha
       
        saida.write(linha_transformada + '\n')# Escrever a linha transformada no arquivo de saída

print(f'Arquivos salvos em {arquivo_saida}')
