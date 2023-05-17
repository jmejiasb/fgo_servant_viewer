import re

from .fgo_api import FgoApi 

class ServantModel(FgoApi):

    def __init__(self):
        self.fgo = FgoApi()
        self.list_regions = self.fgo.regions
        self.list_classes = self.fgo.classes
        self.list_rarities = self.fgo.rarities

    def filterServant(self, region=str, className=str, rarity=int):
        filtered_servants = []
        servants = self.fgo.servants[region]

        for servant in servants:
            if servant["className"] == className and servant["rarity"] == rarity:
                    filtered_servants.append(servant["name"])

        return filtered_servants
    
    def getServantImage(self,stage, servant):

        image_url = servant["extraAssets"]["charaGraph"]["ascension"][str(stage)]
        
        return self.fgo.get_image(image_url).content

    def getServantAlignment(self,servant):
        
        first_alignment = servant["traits"][3]["name"]
        second_alignment = servant["traits"][4]["name"]

        servant_alignment = re.split('(?<=.)(?=[A-Z])', first_alignment)[1] + " " + re.split('(?<=.)(?=[A-Z])', second_alignment)[1]

        return servant_alignment

if __name__ == "__main__":

    model = ServantModel()
    model.filterServant("NA", "saber", 5)
    
    print(model.filtered_servants)
