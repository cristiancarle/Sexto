from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el navegador
driver = webdriver.Chrome()

# Ir a la página de login
driver.get("https://the-internet.herokuapp.com/login")

# Esperar unos segundos para que cargue
time.sleep(1)

# Ingresar el nombre de usuario
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")

# Ingresar la contraseña
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")

# Hacer clic en el botón de Login
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

# Esperar un poco para que cargue la nueva página
time.sleep(2)

# Verificar que aparezca el mensaje de éxito
success_message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in success_message:
    print("✅ Prueba exitosa: login correcto")
else:
    print("❌ Prueba fallida: no se mostró el mensaje esperado")

# Cerrar el navegador
driver.quit()
