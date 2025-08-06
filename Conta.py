class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = 0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('O saldo não pode ser negativo')
        else:
            self._saldo = saldo

    def saque(self, valor):
        print('=========SAQUE========')
        if self._saldo>= valor:
            self._saldo -= valor
            print('Saldo: ', self._saldo)
            print('Saque concluído')
        else:
            print('Saldo insuficiente')
        print('========================')
      
    def depositar(self, valor):
        self._saldo += valor
      
    def extrato(self):
        print('=========EXTRATO========')
        print('Cliente: ', self.titular)
        print('Saldo atual: ', self._saldo)
        print('===============================')
