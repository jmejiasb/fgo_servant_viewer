import requests

class FgoApi:

    base_url = 'https://api.atlasacademy.io/'

    def __init__(self):
        self.servants = {}
        self.__get_list_of_servants()
        self.regions = list(self.servants.keys())
        self.__get_servant_classes()
        self.__get_servant_rarities()

    def __get_list_of_servants(self):

        #Get processed data for both NA and JP
        self.na_endpoint = 'export/NA/basic_servant.json'
        self.jp_endpoint = 'export/JP/basic_servant_lang_en.json'

        self.__append_servants(self.na_endpoint)
        self.__append_servants(self.jp_endpoint)

    def __append_servants(self,endpoint=str):
        
        response = requests.get(FgoApi.base_url + endpoint).json()

        server = endpoint[7:9]
        self.servants[server] = response

        self.servants[server]

    def __get_servant_classes(self):

        self.classes = set()

        #Se obtiene las clases desde el servidor de JP porque es el mas actualizado
        for servant in self.servants["JP"]:
            self.classes.add(servant["className"])
        
        self.classes = list(self.classes)
        self.classes.sort()

    def __get_servant_rarities(self):

        self.rarities = set()

        for servant in self.servants["JP"]:
            self.rarities.add(str(servant["rarity"]))
        
        self.rarities = list(self.rarities) 
        self.rarities.sort()

    def get_servant(self,region=str,servant_id=int):

        endpoint = f'nice/{region}/servant/{servant_id}'

        params = {
            "lore":"false",
            "lang":"en"
        }

        response = requests.get(FgoApi.base_url + endpoint, params=params)

        return response.json()
    
    def get_image(self,image_url=str):

        response = requests.get(image_url)

        return response
    
    def get_id_by_name(self, server=str, name=str):
        list_server = self.servants[server]
        for servant in list_server:
            if servant["name"] == name:
                return servant["id"]
                break


#Test
if __name__ == '__main__':

    fgo = FgoApi()
    servant = fgo.get_servant('JP', 1000200)
    servant_image_url = servant["extraAssets"]["charaGraph"]["ascension"]["1"]
    fgo.get_id_by_name("JP","Miss Crane")

    print(servant_image_url)
    #print(id)
    print("Done!")