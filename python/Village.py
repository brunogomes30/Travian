from resources_utils import *
from buildings_utils import *
import functions

class Village:
    def __init__(self):
        #Number of village
        self.number = 1
        
        #Resources
        self.resources = []
        self.wood = 0
        self.clay = 0
        self.cereal = 0
        self.iron = 0
        self.cereal_free=0
        
        #Productions
        self.productions = []
        self.wood_prod = 0
        self.clay_prod = 0
        self.cereal_prod = 0
        self.iron_prod = 0
        
        #Storage
        self.storage = 0
        self.cereal_storage = 0
        #others
        self.buildings= {}
        #utils
        self.driver = None
        
        
    
    def refresh_data(self):
        get_resources(self,self.driver)
        #get_buildings(self)
    
    
    def __repr__(self):
        string = "Village %d:\n\tWood(%d)\n\tClay(%d)\n\tIron(%d)\n\tCereal(%d)\n\tCereal_free(%d)" %(self.number,self.wood,self.clay,self.iron,self.cereal,self.cereal_free)
        string += "\n\tStorage(%d)" %self.storage
        string += "\n\tCereal Storage(%d)" %self.cereal_storage
        string += "\n\n\tProduction:\n\t\tWood(%d)\n\t\tClay(%d)\n\t\tIron(%d)\n\t\tCereal(%d)" %(self.wood_prod, self.clay_prod, self.iron_prod, self.cereal_prod)
        return string