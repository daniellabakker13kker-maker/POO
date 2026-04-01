
import random

class Bingo:
    def __init__(self, numBolas):
        self.numBolas = numBolas
        self.bolas = []

    def Proximo(self, numBolas):
        bola_sorteada = randint(1, self.numBolas)
        if bola_sorteada in self.bolas:
            return Proximo(self, numBolas)
        else:
            self.bolas.append(bola_sorteada) 

        if len(self.bolas) == self.numBolas:
            print("Todas as bolas já foram sorteadas")