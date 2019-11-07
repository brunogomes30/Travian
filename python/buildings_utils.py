from main import server
import Village
import Building

def get_buildings(village):
    driver = village.driver
    
    #First get resource production buildings
    driver.get(server+"/dorf1.php")
    areas = driver.find_elements_by_css_selector("#rx > area")
    areas_href = (i.get_attribute("href") for i in areas)
    buildings = []•
    for x in areas_href:
        driver.get(server+"/"x) 
        cost_span = driver.find_elements_by_css_selector("#contract > .resourceWrapper > .resource > .value")
        cost = []
        for i in cost_span:
            cost.append(int(cost_span.text))
        building = Building.Building()
        building.cost = cost
        building.id = get_id(x)
        building.village = village
        building.is_resource = True
        
        buildings.append(building)
        
    