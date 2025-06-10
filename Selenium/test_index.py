from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

file_path = "/home/proa/Python/Cursos/Sexto/Selenium/login.html"
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Abrir el archivo HTML local
    driver.get("file://" + file_path)

    # Completar el formulario
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.TAG_NAME, "button")

    username_input.send_keys("admin")
    password_input.send_keys("1234")
    login_button.click()

    # Esperar un poco a que se actualice el mensaje
    time.sleep(2)

    # Verificar el mensaje de resultado
    message = driver.find_element(By.ID, "message").text
    if "exitoso" in message:
        print("✅ Test de login exitoso.")
    else:
        print("❌ Falló el login.")

finally:
    time.sleep(3)
    driver.quit()