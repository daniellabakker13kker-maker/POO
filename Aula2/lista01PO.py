# AREA E CIRCUFERENCIA
# AEREA FORMULA: a = pi * r^2
# CIRCUFERENCIA: c = 2 * pi * r


class Circulo():
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3
    
    def calculo_area(self):
        area = self.pi*(self.raio**2)
        print(area)

    def calculo_circuferencia(self):
        circunferencia = 2 * self.pi * self.raio
        print(circunferencia)

circulo_1 = Circulo(2)
circulo_1.calculo_area
circulo_1.calculo_circuferencia

