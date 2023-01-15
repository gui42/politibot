import requests

class ApiController:
    url = ''
    # def __init__(self):
    #     self.name = ''

    def setUrl(self, url):
        self.url = url

    def getUrl(self):
        return self.url

    def getBlocos(self, url):
        self.setUrl(url)
        print(self.getUrl)
        r = requests.get(f'{self.getUrl}13')
        return r.json()
    
    def getBlocosById(self, url, id):
        self.setUrl(url)
        print(self.getUrl)
        r = requests.get(f'{self.getUrl}{id}')
        return r.json()

teste = ApiController()
str = "https://dadosabertos.camara.leg.br/api/v2/blocos/"
print(teste.getBlocos(str))