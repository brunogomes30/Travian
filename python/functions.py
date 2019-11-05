from selenium import webdriver
server = "https://ts2.lusobrasileiro.travian.com/"

def make_adventure(driver):
    driver.get(server + "hero.php?t=3")
    adventures = driver.find_elements_by_css_selector(".gotoAdventure")
    if len(adventures) >0:
        adventures[0].click()
        driver.find_element_by_css_selector(".adventureSendButton > div >  .startAdventure").click()


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
def level_resource(name,highOrLow,driver):
    ids = {
            "madeira" : 1,
            "cereais" : 4,
            "barro"   : 2,
            "ferro"   : 3
            }
    if(name !="ferro" and name !="madeira" and name !="barro" and name !="madeira"):
        print(name +"não é um recurso")
        return
    resource_id = ids[name]
    resources = driver.find_elements_by_css_selector("#village_map > .gid"+str(resource_id))
    levels = []
    for r in resources:
        classes = r.get_attribute("class")
        #get index of last 'level'
        print(classes)
        index = classes.find("level",2)
        print(classes)
        level = int(classes[index+5:])
        levels.append((r,level))
    print(levels)
    
    #Sorting...
    if highOrLow ==0:
        levels = sorted(levels, key=lambda x:(x[1]))
    else:
        levels = sorted(levels, key=lambda x:(x[1]), reverse=True)
        
    print(levels)
    count = 1
    href = ""
    arr = driver.find_elements_by_css_selector("#village_map > *")
    for r in arr:
        print(r)
        if( r == levels[0][0]):
            href = "/build.php?id="+str(count)
            break
        count+=1
    print("href="+href)
    driver.get(server + href)
    error_message_list = driver.find_elements_by_css_selector("div.upgradeBlocked > .errorMessage")
    if(len(error_message_list) == 0):
        level_up_building()
    else:
        text = error_message_list[0].text
        day = text[24:26]
        month = text[27:29]
        hour = text[34:36]
        minute = text[37:39]
        print(day,month,hour,minute)

def level_up_wall(driver):
    driver.get(server + "/build.php?id=40")
    level_up_building(driver)
    
    
def level_up_building(driver):
    driver.find_element_by_css_selector("button.green.build").click()
    
    
    