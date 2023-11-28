from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def abrir_hemera(driver, espera):
    login = 'Robo1'
    senha = 'Robo1@'

    # Obter as alças (handles) das abas abertas
    handles = driver.window_handles
    # Mudar para a nova aba
    driver.switch_to.window(handles[1])
    # Abrir uma URL na nova aba
    driver.get("http://10.4.6.237:8080/hemera/hemera.jsp")
    sleep(espera)
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

    sleep(espera)
    driver.switch_to.default_content()
    bt_mais_uc = driver.find_element(By.ID, "ext-gen104")
    bt_mais_uc.click()
    print('clique em bt_mais_uc')

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

# Inicializar o driver do Firefox com as opções
driver = webdriver.Firefox()
driver.execute_script("window.open()")
espera = 2
abrir_hemera(driver, espera)
grupo_a_search(driver, espera)