from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="/home/proa/Python/Cursos/Sexto/Selenium/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")

search_box= driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()