from fgo_api import FgoApi 

class ServantModel:

    def __init__(self):
        self.fgo = FgoApi()
        self.list_regions = self.fgo.regions
        self.list_classes = self.fgo.classes
        self.list_rarities = self.fgo.rarities

    
