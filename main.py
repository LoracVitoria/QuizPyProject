from corregir_gabaritos import Gabarito
from quiz import Quiz


class GeradorQuiz:
        def __init__(self):
            self.dificuldade = 0
            self.quiz = Quiz()
            self.gabarito = Gabarito()


#   PADRÃO 2 FACADE

        def comecar(self):
            self.quiz.criaQuiz()
            self.getDificuldade()
            self.quiz.setDificuldade(self.dificuldade)
            self.quiz.montaQuestao(self.gabarito)
            self.gabarito.imprimeResultadoFinal()

        def getDificuldade(self):
            self.dificuldade = str(input())


if __name__ == '__main__':
    geradorQuiz = GeradorQuiz()
    geradorQuiz.comecar()