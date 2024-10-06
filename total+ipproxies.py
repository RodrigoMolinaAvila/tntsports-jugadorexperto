from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading

# Configura las rutas de los drivers
driver_paths = {
    'edge': './msedgedriver.exe',
    'chrome': './chromedriver.exe',
    'firefox': './geckodriver.exe'
}

# Define el número de iteraciones
num_iteraciones = 1000

# Variables para contar los clics exitosos
clicks = {
    'edge': 0,
    'chrome': 0,
    'firefox': 0
}

# Listas para almacenar los datos de los clics
data = {
    'edge': [],
    'chrome': [],
    'firefox': []
}

# URL de la página web de TNT Sports para realizar la votación
url = "https://tntsports.cl/jugador-experto-easy"

# Función para actualizar el gráfico
def update(frame):
    plt.clf()
    browsers = ['Edge', 'Chrome', 'Firefox']
    clicks_totals = [clicks['edge'], clicks['chrome'], clicks['firefox']]
    
    # Obtener la paleta de colores 'viridis'
    cmap = plt.get_cmap('viridis')
    colors = [cmap(i / len(browsers)) for i in range(len(browsers))]
    
    # Crear histograma
    bars = plt.bar(browsers, clicks_totals, color=colors)
    
    # Agregar etiquetas de totales en cada barra
    for bar, total in zip(bars, clicks_totals):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, str(total), ha='center', va='bottom')
    
    # Mostrar el total de clics exitosos
    total_clicks = sum(clicks_totals)
    plt.text(1, -0.1, f'Total Clics Exitosos: {total_clicks}', ha='center', va='top', fontsize=12, color='black', transform=plt.gca().transAxes)
    
    plt.xlabel('Navegadores')
    plt.ylabel('Clics Exitosos')
    plt.title('Histograma de Clics Exitosos por Navegador')

# Función para ejecutar el código de un navegador
def run_browser(browser):
    global clicks, data
    service_class = {
        'edge': EdgeService,
        'chrome': ChromeService,
        'firefox': FirefoxService
    }
    options_class = {
        'edge': EdgeOptions,
        'chrome': ChromeOptions,
        'firefox': FirefoxOptions
    }
    private_mode = {
        'edge': "--inprivate",
        'chrome': "--incognito",
        'firefox': "--private"
    }

    for i in range(num_iteraciones):
        service = service_class[browser](executable_path=driver_paths[browser])
        options = options_class[browser]()
        options.add_argument(private_mode[browser])
        options.add_argument("--headless")  # Ejecutar en modo sin cabeza (headless)
        driver = webdriver.__dict__[browser.capitalize()](service=service, options=options)

        try:
            driver.get(url)
            wait = WebDriverWait(driver, 10)
            
            # Hacer clic en el elemento de la votación en la página de TNT Sports
            elemento = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#quick-poll-n26 > div.anwsers.oZ8O24vdejA4vhbOK7R-6w\\=\\= > div:nth-child(1)')))
            elemento.click()
            clicks[browser] += 1
            data[browser].append(clicks[browser])
            print(f"Clic {i+1} realizado en {browser.capitalize()}")
            time.sleep(2)
        except Exception as e:
            print(f"Error en {browser.capitalize()}: {e}")
        finally:
            # Eliminar cookies y datos del navegador
            driver.delete_all_cookies()
            driver.quit()
        time.sleep(2)

# Crear hilos para cada navegador
threads = {
    'edge': threading.Thread(target=run_browser, args=('edge',)),
    'chrome': threading.Thread(target=run_browser, args=('chrome',)),
    'firefox': threading.Thread(target=run_browser, args=('firefox',))
}

# Iniciar los hilos
for thread in threads.values():
    thread.start()

# Configurar la animación del gráfico
fig = plt.figure()
ani = FuncAnimation(fig, update, interval=1000)

# Mostrar el gráfico
plt.show()

# Esperar a que los hilos terminen
for thread in threads.values():
    thread.join()
