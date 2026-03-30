# A classe deve ter atributos para armazenar o nome do titular da conta, o número da conta e seu saldo e métodos
#para realizar as operações de depósito e saque.

class Conta():
    def __init__(self, nome, numero, saldo):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo

    def deposito(self, dinheiro_dep):
        saldo_novo = self.saldo + dinheiro_dep
        print(f"
                Titular: {self.nome} 
                Numero C: {self.numero}
                Saldo atual: {saldo_novo}")
