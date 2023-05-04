from fgo_api import FgoApi 

class ServantModel(FgoApi):

    def __init__(self):
        self.fgo = FgoApi()
        self.filtered_servants = []
        self.list_regions = self.fgo.regions
        self.list_classes = self.fgo.classes
        self.list_rarities = self.fgo.rarities

    def filterServant(self, region=str, className=str, rarity=int):

        servants = self.fgo.servants[region]

        for servant in servants:
            if servant["className"] == className and servant["rarity"] == rarity:
                self.filtered_servants.append(servant["name"])


if __name__ == "__main__":

    model = ServantModel()
    model.filterServant("NA", "saber", 5)
    
    print(model.filtered_servants)
