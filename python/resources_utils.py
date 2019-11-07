def get_resources(village,driver):
    resources = driver.execute_script("return resources")
    production = resources["production"]
    
    village.productions = list(production.values())
    village.productions.pop()
    village.wood_prod = production["l1"]
    village.clay_prod = production["l2"]
    village.iron_prod = production["l3"]
    village.cereal_prod = production["l4"]
    
    current_resources = resources["storage"]
    village.resources = list(current_resources.values())
    village.wood = current_resources["l1"]
    village.clay = current_resources["l2"]
    village.iron = current_resources["l3"]
    village.cereal = current_resources["l4"]
    village.cereal_free = production["l5"]
    
    maxStorage = resources["maxStorage"]
    village.storage =  maxStorage["l1"]
    village.cereal_storage = maxStorage["l4"]

