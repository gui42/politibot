import requests


class ApiController(object):
    url = ""
    # def __init__(self):
    #     self.name = ''

    def setUrl(self, url):
        self.url = url

    def getUrl(self):
        return self.url


teste = ApiController()
str = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"
str_dep = "https://dadosabertos.camara.leg.br/api/v2/deputados/"
str_legislaturas = "https://dadosabertos.camara.leg.br/api/v2/legislaturas/"
print(teste.getDeputadosLideres(str_legislaturas, 204521))
