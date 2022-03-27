import time

import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
search_url = "https://www.flashscore.es"
driver.get(search_url)
equipo = "Burgos"

time.sleep(3)
#Cookies
driver.find_element(by=By.ID, value='onetrust-accept-btn-handler').click()
time.sleep(4)

#expandir partidos
#driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'mostrar partidos')]").click()
#time.sleep(10)

#Ingresar el nombre del equipo
driver.find_element(by=By.XPATH, value=f"//*[contains(text(), '{equipo}')]").click()
time.sleep(3)
d = driver.current_url
print(d)







