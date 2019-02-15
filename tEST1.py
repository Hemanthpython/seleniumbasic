from selenium import webdriver

browser='Chrome'

if browser=='Chrome':
 driver=webdriver.Chrome()

elif browser== ie :
 driver = webdriver.Ie("C:/Users/Parinitha/Desktop/IE/IEDriverServer.exe")

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_id("email").send_keys("9986544824")
driver.find_element_by_id("pass").send_keys("Test123")
driver.find_element_by_id("day").click()

