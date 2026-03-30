# distancia em km da viagem e o tempo gasto em horas e minutos
# programa tem que calcular a velocidade média da viagem

# recebe -> transforma minuto em km -> soma -> realiza o calculo
# v = (variação de espaço) / variação de tempo


class Viagem():
    def __init__(self, espaço, tempo):
        self.espaço = espaço
        horas, minutos = map(int, tempo.split(':'))
        total_horas = horas + minutos / 60
        self.tempo = total_horas

    def velocidade_media(self):
        vel = self.espaço / self.tempo
        print(vel)

viagem_1 = Viagem(10, "5:10")
viagem_1.velocidade_media()