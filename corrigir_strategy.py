
class CorrigirStrategy:

#   PADRÃO 3 STRATEGY

    @staticmethod
    def corrigirQuestao(tipo: int, questao):
        if questao.tipo == 0:
            respostaUsuario = str(input('Resposta: ')).lower().strip()

            if respostaUsuario == questao.alternativasCorretas.pop(0):
                print("\nParabéns, acertou essa!")
                return 1
            else:
                print("\nInfelizmente você errou a questão '-' \nBoa sorte na próxima!")
                return 0
        elif questao.tipo == 1:
            iCertas = 0
            iRespondidas = 0
            for a in questao.alternativasCorretas:
                respostaUsuario = str(input(': ')).lower().strip()
                iCertas += 1
                if respostaUsuario == a:
                    iRespondidas += 1

            if iCertas == iRespondidas:
                print("Parabéns, você acertou todas as alternativas corretas!")
                return 2
            elif iRespondidas != 0:
                print(f"Parabéns, você acertou {iRespondidas} de {iCertas}!")
                return 1
            else:
                print("Infelizmente você errou todas. '-'\nNão desista!")
                return 0

        elif questao.tipo == 2:
            respostaUsuario = str(input('Digite: ')).lower().strip()

            if (respostaUsuario == questao.alternativasCorretas.pop(0)):
                print("\nParabéns, acertou essa!")
                return 3
            else:
                print("\nInfelizmente você errou a questão '-' \nBoa sorte na próxima!")
                return 0





