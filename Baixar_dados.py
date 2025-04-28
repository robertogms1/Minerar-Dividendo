from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time  # Importar biblioteca para manipular o tempo de espera

# Configurar opções do Chrome
chrome_options = Options()
chrome_options.add_experimental_option(
    "detach", True)  # Mantém a janela aberta

# Inicializar o driver
driver = webdriver.Chrome(options=chrome_options)

# Abrir a página desejada
driver.get("https://statusinvest.com.br/acoes/busca-avancada")

# Localizar o botão "buscar" pelo XPath
btn_buscar = driver.find_element(
    By.XPATH, "//button[contains(@class,'fs-3 pl-2 pr-2 pl-sm-3 pr-sm-3 tooltipped')]")

# Clicar no botão "buscar"
ActionChains(driver).move_to_element(btn_buscar).click(btn_buscar).perform()

# Aguardar 2 segundos
time.sleep(2)

# Localizar o segundo botão pelo XPath
btn_download = driver.find_element(
    By.XPATH, "//i[@class='material-icons left mr-0 mr-sm-2']")

# Clicar no segundo botão
ActionChains(driver).move_to_element(
    btn_download).click(btn_download).perform()
