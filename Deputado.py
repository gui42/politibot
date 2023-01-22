import requests
import ApiController

class Deputado(ApiController):

    def getDeputados(self, url):
        self.setUrl(url)
        r = requests.get(f'{self.getUrl()}')
        return r.json()

    def getDeputadosById(self, url, id):
        self.setUrl(url)
        r = requests.get(f'{self.getUrl()}{id}')
        return r.json()
    
        """
            Retorna os registros de pagamentos e reembolso do 
            carinha feitas em prol da câmara, identificado pela
            {id} do manolo.
        """
    def getDeputadosDespesas(self, url, id):
        self.setUrl(url)
        url_complen = '/despesas?ordem=ASC&ordenarPor=ano'
        r = requests.get(f'{self.getUrl()}{id}{url_complen}')
        return r.json()

    def getDeputadosDiscursos(self, url, id):
        self.setUrl(url)
        url_complen = '/discursos?ordenarPor=dataHoraInicio&ordem=ASC'
        r = requests.get(f'{self.getUrl()}{id}{url_complen}')
        return r.json()
    
    def getDeputadosEventos(self, url, id):
        self.setUrl(url)
        url_complen = '/eventos?ordem=ASC&ordenarPor=dataHoraInicio'
        r = requests.get(f'{self.getUrl()}{id}{url_complen}')
        return r.json()
    
    def getDeputadosFrentes(self, url, id):
        self.setUrl(url)
        url_complen = '/frentes'
        r = requests.get(f'{self.getUrl()}{id}{url_complen}')
        return r.json()

    def getDeputadosOcupacoes(self, url, id):
        self.setUrl(url)
        url_complen = '/ocupacoes'
        r = requests.get(f'{self.getUrl()}{id}{url_complen}')
        return r.json()
    
    def getDeputadosOrgaos(self, url, id):
        self.setUrl(url)
        url_complen = '/orgaos?ordem=ASC&ordenarPor=dataInicio'
        r = requests.get(f'{self.getUrl()}{id}{url_complen}')
        return r.json()

    def getDeputadosProfissoes(self, url, id):
        self.setUrl(url)
        url_complen = '/profissoes'
        r = requests.get(f'{self.getUrl()}{id}{url_complen}')
        return r.json()

    def getDeputadosLideres(self, url, id):
        self.setUrl(url)
        url_complen = '/lideres'
        r = requests.get(f'{self.getUrl()}{id}{url_complen}')
        return r.json()