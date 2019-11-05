from selenium import webdriver
import functions

username = "ultracg"
password = "12345"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("C:\\Users\\ultra\\OneDrive\\Desktop\\chromedriver.exe") #,chrome_options=chrome_options

driver.get("https://ts2.lusobrasileiro.travian.com/")
    
driver.find_element_by_name("name").send_keys(username)
driver.find_element_by_name("password").send_keys(password)

driver.find_element_by_id("s1").click()

functions.make_adventure(driver)
#functions.level_resource("barro",0,driver)
