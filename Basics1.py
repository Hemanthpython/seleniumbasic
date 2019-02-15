from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
time.sleep(5)
print(driver.title)
print(driver.current_url)
print(driver.minimize_window())
time.sleep(5)
print(driver.maximize_window())