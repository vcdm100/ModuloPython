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
        print(f"Saldo antes da conversão para real: {self.saldo:,.2f}");
        valorEmReal = f'R$ {self.saldo:_.2f}';
        valorEmReal = valorEmReal.replace('.',',').replace("_",".")
        print(f"Saldo: {valorEmReal}");
        
#Criação de uma conta e realização de operações - VICTOR
conta = Conta(123, "Victor");

conta.depositar(1000);
conta.sacar(500);
conta.exibir_informacoes();
print("----------------")
#Criação de uma conta e realização de operações - VINICIUS
conta = Conta(321, "Vinicius",2000);

conta.depositar(400);
conta.sacar(2500);
conta.exibir_informacoes();
print("----------------")

#Criação de uma conta e realização de operações - SIMONE
conta = Conta(231, "Simone",1300000);

conta.depositar(8000);
conta.sacar(2500);
conta.exibir_informacoes();

""" RESULTADO (TERMINAL)

Conta: 123
titular: Victor
Saldo antes da conversão para real: 500.00
Saldo: R$ 500,00
----------------
Saldo insuficiente!
Conta: 321
titular: Vinicius
Saldo antes da conversão para real: 2,400.00
Saldo: R$ 2.400,00
----------------
Conta: 231
titular: Simone
Saldo antes da conversão para real: 1,305,500.00
Saldo: R$ 1.305.500,00

"""