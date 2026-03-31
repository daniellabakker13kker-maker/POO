# A classe deve ter atributos para armazenar o nome do titular da conta, o número da conta e seu saldo e métodos
#para realizar as operações de depósito e saque.

class Conta():
    def __init__(self, nome, numero, saldo):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo

    def deposito(self, dinheiro_dep):
        self.saldo += dinheiro_dep
        print(f"Titular: {self.nome} \nNumero C: {self.numero} \nSaldo atual: {self.saldo}")

    def saque(self, dinheiro_remov):
        self.saldo -= dinheiro_remov
        print(f"Titular: {self.nome} \nNumero C: {self.numero} \nSaldo atual: {self.saldo}")


cliente = Conta("Luz", 2223334, 500)
cliente.saque(500)