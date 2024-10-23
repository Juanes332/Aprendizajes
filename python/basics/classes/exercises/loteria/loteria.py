from random import choice


class Boleto:

    def __init__(self, digito):
        self.digito = digito
        self.loteria = [3, 5, 6, 2, 3, 69, 85,
                        96, 246, 96, 'l', 'f', 'u', 'j', 't']
        self.win = choice(self.loteria)

    def aleatorio(self):
        mi_boleto = self.digito

        if mi_boleto == self.win:
            return f'Haz ganado la loteria con {mi_boleto}'
        else:
            return f'Prueba de nuevo'

    def analisis(self):
        for winer in self.loteria:
            print(winer)


boleto1 = Boleto('l')
print(boleto1.aleatorio())
print(boleto1.analisis())
