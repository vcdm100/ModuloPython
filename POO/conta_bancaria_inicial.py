#Solução orientada a objetos para um banco com a entidade "Conta"

class Conta:
    def __init__ (self, numero, titular, saldo = 0):
        self.numero = numero;
        self.titular = titular;
        self.saldo = saldo;
    
    def depositar(self, valor):
        self.saldo += valor;
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor;
        else:
            print("Saldo insuficiente!");
        
    def exibir_informacoes(self):
        print(f"Conta: {self.numero}");
        print(f"titular: {self.titular}");
        print(f"Saldo: {self.saldo:,.2f}");
        
#Criação de uma conta e realização de operações
conta = Conta(123, "Victor");

conta.depositar(1000);
conta.sacar(500);
conta.exibir_informacoes();

""" RESULTADO (TERMINAL)

Conta: 123
titular: Victor
Saldo: 500.00

"""
        