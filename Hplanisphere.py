from selenium import onclick
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.maximize_window()

driver.get("https://hotel.testplanisphere.dev/ja/login.html"); 
driver.find_element_by_id("email").send_keys("yoshiki@example.com")
driver.find_element_by_id("password").send_keys("pass-pass")

driver.find_element_by_id("login-button").click() 

driver.close() 
