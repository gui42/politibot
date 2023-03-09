from pprint import pprint


from Partidos import Partidos

partidos = Partidos()
teste = partidos.partidos(sigla=['pt', 'pl'])
pprint(teste)
