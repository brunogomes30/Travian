class Building:
    def __init__(self):
        self.designation =""
        self.href = ""
        self.is_resource = False
        self.level = 1
        self.cost = [0,0,0,0,0]
        self.time = 0
        self.village = None
        
    def __repr__(self):
        return str(self.href) + "\n"+str(self.cost)