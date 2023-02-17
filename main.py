import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Launch the web browser and navigate to the login page
PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.saucedemo.com/")

time.sleep(3)
# Enter your email and password into the input fields
userName_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]' )))
userName_input.send_keys("standard_user")
time.sleep(3)
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
password_input.send_keys("secret_sauce")

# Click the login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
login_button.click()

time.sleep(3)

count = 1
time.sleep(3)
add_to_cart_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')))
add_to_cart_button.click()
time.sleep(3)
add_to_cart_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))
add_to_cart_button.click()
time.sleep(3)


click_cart_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
click_cart_button.click()
time.sleep(3)
checkout_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]')))
checkout_button.click()
time.sleep(3)
firstName_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]' )))
firstName_input.send_keys("Ridwanur")
time.sleep(3)
lastName_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]' )))
lastName_input.send_keys("Rahman")
time.sleep(3)
zip_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]' )))
zip_input.send_keys("1234")
time.sleep(3)
continue_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]')))
continue_button.click()
time.sleep(3)
finish_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]')))
finish_button.click()
time.sleep(3)

driver.quit()