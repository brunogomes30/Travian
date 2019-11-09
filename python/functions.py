from selenium import webdriver
server = "https://ts2.lusobrasileiro.travian.com/"
from Village import *
from Building import *
from buildings_utils import *

resources_tupple = ("madeira","barro","ferro","cereais")

def make_adventure(driver):
    try:
        driver.get(server + "hero.php?t=3")
        adventures = driver.find_elements_by_css_selector(".gotoAdventure")
        if len(adventures) >0:
            adventures[0].click()
            driver.find_element_by_css_selector(".adventureSendButton > div >  .startAdventure").click()
        return True
    except Exception:
        return False


def set_hero_resources(resource,driver):
    ids = {
            "todos"  : 0,
            "madeira": 1,
            "barro"  : 2,
            "ferro"  : 3,
            "cereais": 4    
            }
    index = ids[resource]
    driver.get(server + "hero.php")
    driver.find_element_by_css_selector(".resource.r"+str(index)).click()
    driver.find_element_by_name("saveHeroAttributes").click()


#Falta guardar o tempo para quando pode evoluir
def level_best_resource(village):
    driver = village.driver
    driver.get(server + "dorf1.php")    
    prod_res = order_resources(village)
    
    for i in range(len(prod_res)):
        t = prod_res[i]
        if(level_resource(resources_tupple[t[0]],0,driver)):
            if(i<3):
                level_resource(resources_tupple[prod_res[i+1][0]],0,driver)
            break

#Returns a list with [index,production,stock]
def order_resources(village):
    productions = village.productions
    resources = village.resources
    prod_res = list([i,productions[i],resources[i]] for i in range(4))
    
    prod_res = sorted(prod_res, key=lambda x:(x[1]+ x[2]/8))
    for x in prod_res:
        print((x[1]+ x[2]/8),end=" ")
    print()
    print(prod_res)
    return prod_res

def level_resource(name,highOrLow,driver):
    ids = {
            "madeira" : 1,
            "cereais" : 4,
            "barro"   : 2,
            "ferro"   : 3
            }
    if(name !="ferro" and name !="madeira" and name !="barro" and name !="cereais"):
        print(name +"não é um recurso")
        return
    resource_id = ids[name]
    resources = driver.find_elements_by_css_selector("#village_map > .gid"+str(resource_id))
    levels = []
    for r in resources:
        classes = r.get_attribute("class")
        #get index of last 'level'
        #print(classes)
        index = classes.find("level",2)
        #print(classes)
        level = int(classes[index+5:])
        
        if("underConstruction" in classes):
            level +=1
            
        levels.append((r,level))
    #print(levels)
    
    #Sorting...
    if highOrLow ==0:
        levels = sorted(levels, key=lambda x:(x[1]))
    else:
        levels = sorted(levels, key=lambda x:(x[1]), reverse=True)
        
    #print(levels)
    count = 1
    href = ""
    arr = driver.find_elements_by_css_selector("#village_map > *")
    for r in arr:
        #print(r)
        if( r == levels[0][0]):
            href = "/build.php?id="+str(count)
            break
        count+=1
    #print("href="+href)
    driver.get(server + href)
    error_message_list = driver.find_elements_by_css_selector("div.upgradeBlocked > .errorMessage")
    gold_builder_list = driver.find_elements_by_css_selector(".section1 > .gold.builder")
    print("GOLD",len(gold_builder_list))
    if(len(gold_builder_list)>0):
        return False
    if(len(error_message_list) == 0):
        level_up_building(driver)
        return True
    else:
        text = error_message_list[0].text
        
        day = int(text[24:26])
        month = int(text[27:29])
        hour = int(text[34:36])
        minute = int(text[37:39])
        
        print(day,month,hour,minute)
        return False

def level_up_wall(driver):
    driver.get(server + "/build.php?id=40")
    level_up_building(driver)
    
    
def level_up_building(driver):
    try:
        driver.find_element_by_css_selector("button.green.build").click()
    except Exception:
        print("Erro a level_up_building")
    
    
    