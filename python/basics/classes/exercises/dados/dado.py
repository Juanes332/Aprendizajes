from random import randint


class Dados:

    def __init__(self, caras=6):
        self.caras = caras

    def tirar_dado(self):
        cara_aleatoria = randint(1, self.caras)

        return cara_aleatoria


dado1 = Dados()
print(dado1.tirar_dado())

dado2 = Dados(caras=10)
print(dado2.tirar_dado())

dado3 = Dados(caras=20)
print(dado3.tirar_dado())
