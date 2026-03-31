class Circulo:
    def __init__(self):
        self._raio = 0.0

    def set_raio(self, raio):
        self._raio = raio

    def get_raio(self):
        print(self._raio)

    def calc_area(self):
        area = 3.14 * (self._raio ** 2)
        print(area)
    
    def calc_circunferencia(self):
        circuferencia = 2 * 3.14 * self._raio
        print(circuferencia)

forma1 = Circulo()
forma1.set_raio(2)
forma1.get_raio()
forma1.calc_area()
forma1.calc_circunferencia()
forma1.set_raio(5)
forma1.get_raio()
forma1.calc_area()
forma1.calc_circunferencia()



