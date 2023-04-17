import requests
import os

class Fgo_Api:

    base_url = 'https://api.atlasacademy.io/'

    def __init__(self):
        self.servants = {}
        self._get_list_of_servants()

    def _get_list_of_servants(self):

        #Get processed data for both NA and JP
        self.na_endpoint = 'export/NA/basic_servant.json'
        self.jp_endpoint = 'export/JP/basic_servant_lang_en.json'

        self.__append_servants(self.na_endpoint)
        self.__append_servants(self.jp_endpoint)

    def __append_servants(self,endpoint=str):
        
        response = requests.get(Fgo_Api.base_url + endpoint).json()

        server = endpoint[7:9]
        self.servants[server] = response

        self.servants[server]

    def get_servant(self,region=str,servant_id=int):

        endpoint = f'nice/{region}/servant/{servant_id}'

        params = {
            "lore":"false",
            "lang":"en"
        }

        response = requests.get(Fgo_Api.base_url + endpoint, params=params)

        return response.json()


if __name__ == '__main__':

    fgo = Fgo_Api()
    servant = fgo.get_servant('JP',504600)
    
    print(fgo.servants['NA'])
    print(servant)