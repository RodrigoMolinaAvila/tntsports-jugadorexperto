from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura la ruta del chromedriver
chrome_driver_path = './chromedriver.exe'  # Cambia esto si `chromedriver.exe` está en otro lugar

num_iteraciones = 10  # Define el número de iteraciones

for i in range(num_iteraciones):
    # Configura el servicio de Chrome
    service = ChromeService(executable_path=chrome_driver_path)

    # Configura las opciones para abrir Chrome en modo incógnito
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")

    # Inicia Chrome con las opciones configuradas
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Abre la página web
        url = "https://viz.flowics.com/public/c5227423dba55186a0b6764930612369/62290fd8069695d8f502cc90/live?fluid=false#embed&uuid=HUNMUXOWRuOseP7dWxe8Ww%3D%3D%7C1714500347873%7Cv1"
        driver.get(url)

        # Espera hasta que el elemento esté presente en la página
        wait = WebDriverWait(driver, 2)  # Espera hasta 2 segundos si es necesario
        elemento = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#quick-poll-n26 > div.anwsers.oZ8O24vdejA4vhbOK7R-6w\\=\\= > div:nth-child(20)'))) # Cambiar el número por el jugador correspondiente

        # Realiza el clic en el elemento
        elemento.click()
        print(f"Clic {i+1} realizado")
        
        # Espera un poco antes de cerrar el navegador, si es necesario
        time.sleep(2)  # Ajusta el tiempo según lo necesario
    
    finally:
        # Cierra el navegador
        driver.quit()

    # Espera un poco antes de abrir una nueva ventana, si es necesario
    time.sleep(0.5)  # Ajusta el tiempo según lo necesario