class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente('Anna', '62982108048')
conta = Conta(c1._nome, 70891, 0)

print(conta.titular,'\n','Número: ',conta.numero,'\n','Saldo: ',conta.saldo)
print('telefone: ',c1._telefone)
conta.depositar(100)
conta.saque(50)
conta.extrato()
