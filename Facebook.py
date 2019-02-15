from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element_by_id('email').send_keys("9986544824")
driver.find_element_by_id('pass').send_keys("tEXT1234")
driver.find_element_by_id('u_0_2').click()
time.sleep(12)