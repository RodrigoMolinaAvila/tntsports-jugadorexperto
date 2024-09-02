from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura la ruta del msedgedriver
driver_path = './msedgedriver.exe'  # Cambia esto si `msedgedriver.exe` está en otro lugar

# Define el número de iteraciones
num_iteraciones = 100

for i in range(num_iteraciones):
    # Configura el servicio de Microsoft Edge
    service = Service(executable_path=driver_path)

    # Configura las opciones para abrir Microsoft Edge en modo incógnito
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--inprivate")

    # Inicia Microsoft Edge con las opciones configuradas
    driver = webdriver.Edge(service=service, options=edge_options)

    try:
        # Abre la página web
        url = "https://viz.flowics.com/public/c5227423dba55186a0b6764930612369/62290fd8069695d8f502cc90/live?fluid=false#embed&uuid=HUNMUXOWRuOseP7dWxe8Ww%3D%3D%7C1714500347873%7Cv1"
        driver.get(url)

        # Espera hasta que el elemento esté presente en la página
        wait = WebDriverWait(driver, 2)  # Espera hasta 15 segundos si es necesario
        elemento = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#quick-poll-n26 > div.anwsers.oZ8O24vdejA4vhbOK7R-6w\\=\\= > div:nth-child(20)'))) #cambiar el nuúmero por el jugador correspondiente

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

