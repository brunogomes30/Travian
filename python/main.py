server = "https://ts2.lusobrasileiro.travian.com/"
from selenium import webdriver
from threading import Timer
from Village import Village
import random
import functions
import os

#reload(Village)

username = "ultracg"
password = "12345"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

#functions.level_resource("madeira",0,driver)
#print(driver.execute_script("return resources;")["production"]["l1"])
def teste(arg):
    print(arg)

#t = Timer(5,teste, ["hello"],{arg:})
#t.start()
village = Village()
def init():
    global village
    driver = webdriver.Chrome(os.getcwd()+"\\webdriver\\chromedriver.exe") #,chrome_options=chrome_options
    driver.get("https://ts2.lusobrasileiro.travian.com/")
    #login
    driver.find_element_by_name("name").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("s1").click()
    village.driver = driver
    village.refresh_data()
    print(village)

#init()

def loop():
    global driver,village
    driver = webdriver.Chrome("webdriver\\chromedriver.exe",chrome_options = chrome_options) #,chrome_options=chrome_options 
    driver.get("https://ts2.lusobrasileiro.travian.com/")
    driver.find_element_by_name("name").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("s1").click()
    village.driver = driver
    village.refresh_data()
    print(village)
    functions.make_adventure(driver)
    functions.level_best_resource(village)
    driver.get("https://ts2.lusobrasileiro.travian.com/build.php?id=28")
    functions.level_up_building(driver)
    if(len(driver.find_elements_by_css_selector(".att2")) > 0):
        try:
            driver.get("https://ts2.lusobrasileiro.travian.com/build.php?id=39&tt=2&z=95301")
            troops_a = driver.find_elements_by_css_selector("#troops > tbody >tr > td > a")
            for a in troops_a:
                a.click()
            driver.find_element_by_id("btn_ok").click()
            driver.find_element_by_id("btn_ok").click()
        except Exception:
            print("Can't attack")
        
    driver.close()
    t = Timer(random.randint(1200,1800),loop)
    t.start()
loop()
#print(driver.find_element_by_css_selector("#production > tbody > tr:first-child > .num").text[1:-1])
#t = Timer(10,hello_world)
#print("start")
#t.start()

#functions.make_adventure(driver)
#functions.level_resource("barro",0,driver)
