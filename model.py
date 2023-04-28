from fgo_api import FgoApi 

class ServantModel:

    def __init__(self):
        self.fgo = FgoApi()
        self.filtered_servant = []
        self.list_regions = self.fgo.regions
        self.list_classes = self.fgo.classes
        self.list_rarities = self.fgo.rarities

    def filter_servant(self, region, className, rarity):

        servants = self.fgo.servants[region]

        for servant in servants:
            if servant["className"] == className and servant["rarity"] == rarity:
                self.filtered_servant.append(servant["name"])


if __name__ == "__main__":

    model = ServantModel()
    model.filter_servant("NA", "saber", 5)
    
    print(model.filtered_servant)
