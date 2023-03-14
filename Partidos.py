import requests


class Partidos:
    def __init__(self, order: str = "ordem=ASC", ordenarPor: str = "&ordenarPor=sigla"):
        self._url = "https://dadosabertos.camara.leg.br/api/v2/partidos"
        self._order = order

    def partidos(
        self,
        sigla: list = [],
        dataInicio: str = "",
        dataFim: str = "",
        idLegislatura: int = "",
        pagina: int = 1,
        itens: int = 100,
        ordem: str = "",
        ordenarPor: str = "",
    ):
        url = f"{self._url}"

        sigla_map = ''
        for si in sigla:
            sigla_map += f"sigla={si}&"

        dataInicio_m = ''
        if dataInicio:
            dataInicio_m = f"dataInicio={dataInicio}&"

        ulr_completa = f"{url}?{dataInicio_m}{sigla_map}{self._order}"
        response = requests.get(ulr_completa)
        return response.json()

    def membros(self, sigla:int=0):
        if not sigla:
            raise ValueError("sigla é obrigatório")
        url = f"{self._url}/{sigla}/membros"
        response = requests.get(url)
        return response.json()
        

