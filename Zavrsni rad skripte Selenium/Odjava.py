from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
#print("Upisite ime ili prezime zaposlenog: ")
#d = input("")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://puppies-closet.com/evidencija/login.php")
korisnicko_ime = driver.find_element(By.NAME, "username").send_keys("ajdinfranca")
password = driver.find_element(By.NAME, "password").send_keys("ajdinfranca123")
login_button = driver.find_element(By.NAME, "login").click()
driver.implicitly_wait(20)
odjava = driver.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul.logout").click()
time.sleep(5)
driver.close()


