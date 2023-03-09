import ApiController
import requests


class Bloco(ApiController):
    def getBlocos(self, url):
        self.setUrl(url)
        print(self.getUrl())
        r = requests.get(f"{self.getUrl()}13")
        return r.json()

    """
        Retorna uma lista de dados básicos sobre deputados que estiveram
        -> em exercício parlamentar em algum intervalo de tempo.
        Se não for passado um parâmetro de tempo, como idLegislatura ou dataInicio,
        -> a lista enumerará somente os deputados em exercício no momento da requisição.
    """

    def getBlocosById(self, url, id):
        self.setUrl(url)
        r = requests.get(f"{self.getUrl()}{id}")
        return r.json()
