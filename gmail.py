from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_id('identifierId').send_keys("kumar.sai4000@gmail.com")
driver.find_element_by_id("identifierNext").click()
driver.find_element_by_id('password').send_keys("Hanuman@1234")





# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# # driver.find_element_by_id('email').send_keys("9986544824")
# # driver.find_element_by_id('pass').send_keys("tEXT1234")
# # driver.find_element_by_id('u_0_2').click()
# # time.sleep(12)driver
# driver.maximize_window()


test 2 :

from selenium import webdriver

browser=='Chrome'
if browser=='Chrome':
    driver=webdriver.chrome()


# elif browser=='ff':
#  driver=webdriver.Firefox(executable path"C:\Users\Parinitha\Desktop\IE\IEDriverServer.exe")

elif browser=='ie':
 driver=webdriver.Ie(executable_path="C:/Users/Parinitha/Desktop/IE/IEDriverServer.exe")

driver.get("https://www.facebook.com/")
driver.maximize_window()


