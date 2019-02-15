from selenium import webdriver


driver = webdriver.Chrome()
# driver.get("file:///C:/Users/Parinitha/Desktop/New App.html")
# driver.find_element_by_id('sid').send_keys("Test")
# driver.find_element_by_id('pid').send_keys("Test123")
# driver.find_element_by_id('bid').click()

driver.get("file:///C:/Users/Parinitha/Desktop/New%20App.html")
driver.find_element_by_id('sid').send_keys("Test")
driver.find_element_by_id('pid').send_keys("Test123")
driver.find_element_by_id('bid').click()