from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as py
import time

def abrir_hemera(driver, espera):
    login = 'Robo1'
    senha = 'Sangue@laranja'

    # Obter as alças (handles) das abas abertas
    handles = driver.window_handles
    # Mudar para a nova aba
    driver.switch_to.window(handles[1])
    # Abrir uma URL na nova aba
    driver.get("http://10.4.6.237:8080/hemera/hemera.jsp")
    sleep(espera)
    driver.maximize_window()
    campo_login = driver.find_element(By.NAME, "username")
    campo_login.clear()
    campo_login.send_keys(login)
    campo_senha = driver.find_element(By.NAME, "password")
    campo_senha.clear()
    campo_senha.send_keys(senha)
    botao_login = driver.find_element(By.ID, "divCenterButton")
    botao_login.click()
    print("logado")
    
def grupo_a_search(driver, espera):
    sleep(espera)
    
    botao_grupo_a = driver.find_element(By.ID, "ext-gen104")
    botao_grupo_a.click()
    print('clique em botao_grupo_a')
    sleep(espera)
    botao_lupa_vermelha = driver.find_element(By.ID, "ext-gen56")
    botao_lupa_vermelha.click()
    print('clique em botao_lupa_vermelha')
    sleep(espera)
    
    driver.switch_to.frame("SEARCH_GROUP_A")
    
    botao_mais_cliente = driver.find_element(By.XPATH, "//legend[@id='ext-gen31']//div[@class='x-casextension-x-button-collapse-expand']")
    botao_mais_cliente.click()
    print('clique em botao_mais_cliente')
    sleep(espera)
    campo_contrato = driver.find_element(By.ID, "ext-comp-1004")
    campo_contrato.clear()
    campo_contrato.send_keys('94648085')
    sleep(espera)
    botao_pesquisar = driver.find_element(By.ID, "ext-gen596")
    botao_pesquisar.click()
    print('clique em botao_pesquisar')

    # sleep(espera)
    # driver.switch_to.default_content()
    # bt_mais_uc = driver.find_element(By.ID, "ext-gen104")
    # bt_mais_uc.click()
    # print('clique em bt_mais_uc')

    print('inicio sleep de 10')
    print('################################################################################################')
    sleep(10)
    
    # botao_tipo_download = driver.find_element(By.XPATH, "//img[@src='../imgs/hemera/export.png']")
    # botao_tipo_download.click() ext-gen605
    
    # botao_tipo_arquivo = driver.find_element(By.ID, "ext-gen149")
    # botao_tipo_arquivo.click()
    
    # sleep(1)
    
    # tipo_arquivo = driver.find_element(By.XPATH, "//div[@class='x-combo-list-item' and contains(text(), 'Arquivo CSV')]")
    # tipo_arquivo.click()
    
    # botao_download = driver.find_element(By.ID, "ext-gen170")
    # botao_download.click()
    
    # sleep(5)
    # driver.quit()
def pesquisa_telemetria(driver, espera, telemetria):#essa função termina com as infos do cliente exibidas no frame do meio
    sleep(espera)
    driver.switch_to.default_content()
    
    esperar_tela('hemera_imagens/tela_inicial_pesquisa.PNG')
    sleep(espera)
    botao_grupo_a = driver.find_element(By.ID, "ext-gen104")
    botao_grupo_a.click()
    print('clique em botao_grupo_a')
    sleep(espera)
    botao_lupa_vermelha = driver.find_element(By.ID, "ext-gen56")
    botao_lupa_vermelha.click()
    print('clique em botao_lupa_vermelha')
    sleep(espera)
    driver.switch_to.frame("SEARCH_GROUP_A")
    bt_mais_telemetria = driver.find_element(By.XPATH, "//legend[@id='ext-gen38']//div[@class='x-casextension-x-button-collapse-expand']")
    bt_mais_telemetria.click()
    print('clique em bt_mais_telemetria')
    sleep(espera)
    campo_min = driver.find_element(by=By.NAME, value="mdl_min")
    campo_min.clear()
    campo_min.send_keys(telemetria)
    sleep(espera)
    botao_pesquisar = driver.find_element(By.ID, "ext-gen596")
    botao_pesquisar.click()
    print('clique em botao_pesquisar')
    sleep(espera)
    esperar_tela("hemera_imagens/bt_mais_pesquisa.PNG")
    bt_path = "hemera_imagens/bt_mais_pesquisa.PNG"  # Caminho do botão para selecionar o cliente
    bt_position = py.locateOnScreen(bt_path, confidence= 0.6)# Procurar a imagem bt_mais_pesquisa 
    py.moveTo(bt_position, duration=0.3)#move cursor até o centro da tela inicial
    py.moveRel(25, 0)
    py.click()#clica no botao para selecionar medidor
    esperar_tela('hemera_imagens/fim_pesquisar_telemetria.PNG')# aguarda carregar a pesquisa
def remover_telemetria():
    sleep(2)
    esperar_tela('hemera_imagens/check_bt_registro.PNG')
    check_path = "hemera_imagens/check_bt_registro.PNG"  # Caminho do botão para selecionar o registro
    check_position = py.locateOnScreen(check_path, confidence= 0.8)# Procurar a imagem check_bt_registro 
    py.moveTo(check_position, duration=0.3)#move cursor até o centro da imagem check_bt_registro 
    py.moveRel(-37, -2)
    py.click()#clica no botao check_bt_registro
    
    esperar_tela("hemera_imagens/bt_cadastro.PNG")
    bt_cadastro_path = "hemera_imagens/bt_cadastro.PNG"  # Caminho do botão bt_cadastro
    bt_cadastro_position = py.locateOnScreen(bt_cadastro_path, confidence= 0.6)# Procurar a imagem bt_cadastro
    py.moveTo(bt_cadastro_position, duration=0.3)#move cursor até o centro da imagem bt_cadastro
    py.click()#clica no botao bt_cadastro
    
    esperar_tela("hemera_imagens/bt_medidor.PNG")
    bt_medidor_path = "hemera_imagens/bt_medidor.PNG"  # Caminho do botão bt_medidor
    bt_medidor_position = py.locateOnScreen(bt_medidor_path, confidence= 0.3)# Procurar a imagem bt_medidor
    py.moveTo(bt_medidor_position, duration=0.3)# move cursor até bt_medidor
    py.click()
    
    esperar_tela('hemera_imagens/bt_remover_telemetria.PNG')
    bt_remover_path = "hemera_imagens/bt_remover_telemetria.PNG"  # Caminho do botão bt_remover_telemetria
    bt_remover_position = py.locateOnScreen(bt_remover_path, confidence= 0.6)# Procurar a imagem bt_remover
    py.moveTo(bt_remover_position)#move cursor até o centro da imagem bt_cadastro
    py.click()#clica no botao bt_cadastro
    
    esperar_tela("hemera_imagens/bt_salvar.PNG")
    bt_salvar_path = "hemera_imagens/bt_salvar.PNG"  # Caminho do botão bt_salvar
    bt_salvar_position = py.locateOnScreen(bt_salvar_path, confidence= 0.6)# Procurar a imagem bt_salvar
    py.moveTo(bt_salvar_position, duration=0.3)#move cursor até o centro da imagem bt_cadastro
    py.click()#clica no botao bt_cadastro

def nova_remocao():
    py.hotkey('ctrl', 'f5')
def esperar_tela(imagem):
    while True:
        tela_encontrada = py.locateOnScreen(f"{imagem}", confidence=0.5)
        
        if tela_encontrada:
            print(f'Encontrado:{imagem}')
            return True
        else:
            print(f'Não encontrado:{imagem}')

# Inicializar o driver do Firefox com as opções
driver = webdriver.Firefox()
driver.execute_script("window.open()")
espera = 2
telemetrias_para_remover = ['41985321860', '41992519470',
                            '41992294686']
abrir_hemera(driver, espera)
for telemetria in telemetrias_para_remover:
    pesquisa_telemetria(driver, espera, telemetria)
    remover_telemetria()
    nova_remocao()
print('Todas as telemetrias foram removidas.')
sleep(2)
py.hotkey('alt','f4')
# grupo_a_search(driver, espera)





