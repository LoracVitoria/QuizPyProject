from corrigir_strategy import CorrigirStrategy


class Gabarito():
    def __init__(self):
        self.resultado = 0

    def corrigirQuestao(self, questao):
        self.resultado += CorrigirStrategy.corrigirQuestao(questao.tipo, questao)

    def imprimeResultadoFinal(self):
        print(f'\nResultado Final!!! \nVocê atingiu {self.resultado} pontos!')

