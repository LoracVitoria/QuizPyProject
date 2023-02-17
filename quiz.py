import json

from corregir_gabaritos import Gabarito
from questoes import Questoes
from resposta import Resposta


class Quiz(Questoes):
    _instance = None

    def __init__(self):
        self.resultado = 0
        self.maximoQuestoes = 0
        self.isTrueFalse = False

    #   PADRÃO 1 SINGLETON

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def criaQuiz(self):
        print('                        88            ')
        print()
        print(' ,adPPYb,d8 88       88 88 888888888  ')
        print('a8"    `Y88 88       88 88      a8P"  ')
        print('8b       88 88       88 88   ,d8P\'    ')
        print('"8a    ,d88 "8a,   ,a88 88 ,d8"       ')
        print(' `"YbbdP\'88  `"YbbdP\'Y8 88 888888888  ')
        print('         88                           ')
        print('         88                           ')
        print()
        print('By Carolzita')
        print('\n\n')
        print('Escolha a dificuldade do quiz!')
        print('1. Fácil')
        print('2. Intermediário')
        print('3. Difícil')
        print('Por favor digite apenas o número da opção desejada: ')

    def montaQuestao(self, gabarito: Gabarito):
        data = json.load(open("gabarito.json", encoding='utf8'))
        questoes = data["quiz"]
        index = 0
        for q in questoes:
            index += 1
            if (index > self.maximoQuestoes):
                break

            questao = Questoes(q['enunciado'], q['tipo'])


            print(f'\n{index}. {questao.enunciado}')

            """
            se index maior quiz.options.maxQuestoes
            break
            """

            respostas = q['opcoes']
            for r in respostas:
                resposta = Resposta(r['conteudo'], r['alternativa'], r['correta'])
                questao.addConjuntoRespostas(resposta)
                if questao.tipo != 2:
                    print(f"{resposta.alternativa}) {resposta.conteudo}")
                if resposta.estaCorreta:
                    questao.defineAlternativasCorretas(resposta.alternativa)


            gabarito.corrigirQuestao(questao)



    def setDificuldade(self, dificuldade):
        if (dificuldade == '1'):
            self.maximoQuestoes = 5
        else:
            if (dificuldade == '2'):
                self.maximoQuestoes = 10
            else:
                if (dificuldade == '3'):
                    self.maximoQuestoes = 15
