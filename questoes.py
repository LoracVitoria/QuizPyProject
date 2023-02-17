from resposta import Resposta

class Questoes:
    def __init__(self, enunciado, tipo:int):
        self.enunciado = enunciado
        self.respostas = []
        self.tipo = tipo
        self.alternativasCorretas = []

    def addConjuntoRespostas(self, resposta):
        assert isinstance(resposta,Resposta), "ERRO! Tem que ser uma classe do tipo Resposta"
        self.respostas.append(resposta)

    def retornaConjuntoRespostas(self):
        list(Resposta(self.respostas))

    def defineAlternativasCorretas(self, alternativa:str):
        self.alternativasCorretas.append(alternativa)

