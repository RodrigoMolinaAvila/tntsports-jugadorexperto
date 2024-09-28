import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt

class VotingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Votación de Jugador Experto")

        self.browser_clicks = {"Chrome": 0, "Firefox": 0, "Edge": 0}
        self.votes = []

        self.setup_ui()
        self.update_histogram()

    def setup_ui(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Navegador:").grid(row=0, column=0, sticky=tk.W)
        self.browser_var = tk.StringVar()
        self.browser_combobox = ttk.Combobox(frame, textvariable=self.browser_var)
        self.browser_combobox['values'] = list(self.browser_clicks.keys())
        self.browser_combobox.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Voto para:").grid(row=1, column=0, sticky=tk.W)
        self.vote_var = tk.StringVar()
        self.vote_entry = ttk.Entry(frame, textvariable=self.vote_var)
        self.vote_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        self.add_button = ttk.Button(frame, text="Agregar Voto", command=self.add_vote)
        self.add_button.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    def add_vote(self):
        browser = self.browser_var.get()
        vote = self.vote_var.get()
        if browser and vote:
            self.browser_clicks[browser] += 1
            self.votes.append(vote)
            self.update_histogram()

    def update_histogram(self):
        self.ax.clear()
        browsers = list(self.browser_clicks.keys())
        clicks = list(self.browser_clicks.values())
        self.ax.bar(browsers, clicks)
        self.ax.set_title("Clicks Exitosos por Navegador")
        self.ax.set_xlabel("Navegador")
        self.ax.set_ylabel("Clicks Exitosos")
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()

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