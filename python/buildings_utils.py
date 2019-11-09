server = "https://ts2.lusobrasileiro.travian.com/"
#from main import server
import Village
import Building

def get_buildings(village):
    driver = village.driver
    
    #First get resource production buildings
    driver.get(server+"/dorf1.php")
    areas = driver.find_elements_by_css_selector("#rx > area")
    areas_href = []
    for i in areas:
        areas_href.append(i.get_attribute("href"))
    #areas_href = (i.get_attribute("href") for i in areas)
    resource_buildings = []
    for x in areas_href:
        print(x)
        driver.get(x)
        cost_spans = driver.find_elements_by_css_selector("#contract > .resourceWrapper > .resource > .value")
        cost = []
        for span in cost_spans:
            cost.append(int(span.text))
        building = Building.Building()
        building.cost = cost
        building.href =  x
        building.village = village
        building.is_resource = True
        resource_buildings.append(building)
    print(resource_buildings)
    