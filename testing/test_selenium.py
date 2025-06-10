from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inicializar el navegador (descarga el driver para tu navegador)
driver = webdriver.Chrome()

# Abrir Google
driver.get("https://www.google.com")

# Buscar algo en Google
search_box = driver.find_element("name", "q")
search_box.send_keys("Testing con Selenium")
search_box.send_keys(Keys.RETURN)

# Esperar unos segundos y cerrar
import time
time.sleep(5)
driver.quit()
