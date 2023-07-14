from conta_bancaria_final import Conta

conta = input("Informe o número da conta: ");
titular = input("Informe o titular da conta: ");
saldo = float(input("Informe o saldo da conta: "));

#Criando uma instância da classe
minhaConta = Conta(conta, titular, saldo);

#Realizando operações na conta
depositar = float(input("Informe o valor para depósito: "));
sacar = float(input("Informe o valor de saque: "));

minhaConta.depositar(depositar);
minhaConta.sacar(sacar);
print("-------------------------");

#Exibindo de informações
minhaConta.exibir_informacoes();

""" RESULTADO (TERMINAL)

Informe o número da conta: 123456-0
Informe o titular da conta: Victor Cláudio
Informe o saldo da conta: 5000
Informe o valor para depósito: 2145.78
Informe o valor de saque: 1562.45
-------------------------
Conta: 123456-0
titular: Victor Cláudio
Saldo antes da conversão para real: 5,583.33
Saldo: R$ 5.583,33

"""