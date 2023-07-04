#Exercícios 03

# 1. Escreva um programa que solicite ao usuário dois números inteiros e exiba a soma, subtração, multiplicação e divisão entre esses números.
num1 = int(input("Digite o primeiro número inteiro: "));
num2 = int(input("Digite o segundo número inteiro: "));

soma            = num1 + num2;
subtracao       = num1 - num2;
multiplicacao   = num1 * num2;
divisao         = num1 / num2;

print("Soma: ", soma);
print("Subtração: ", subtracao);
print("Multiplicação: ", multiplicacao);
print("Divisão: ", divisao, "\n");

""" RESULTADO (TERMINAL):

Digite o primeiro número inteiro: 134
Digite o segundo número inteiro: 67
Soma:  201
Subtração:  67
Multiplicação:  8978
Divisão:  2.0 

"""

# 2. Escreva um programa que solicite ao usuário uma temperatura em graus Celsius e verifique se ela está acima do ponto de ebulição da água (100°C). Caso positivo, exiba a mensagem "A água está fervendo!".
temperatura = int(input("Digite a temperatura em graus Celsius: "));

if temperatura > 100:
    print("A água está fervendo!");
    
print();

""" RESULTADO (TERMINAL):

Digite a temperatura em graus Celsius: 150
A água está fervendo!

"""

# 3. Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é par ou ímpar.
num = int(input("Digite um número inteiro: "));

if num % 2 == 0:
  print("Esse número é PAR.");
else:
    print("Esse número é IMPAR.");
    
print();

""" RESULTADO (TERMINAL):

Digite um número inteiro: 6
Esse número é PAR.

Digite um número inteiro: 9
Esse número é IMPAR.

"""

# 4. Escreva um programa que solicite uma senha ao usuário e verifique se a senha está correta. Considere a senha correta como "123456".
senha = input("Digite sua senha: ");

senha_correta = "123456";

if senha == senha_correta:
    print("Usuário logado com sucesso!");
else:
    print("Senha incorreta!");
    
print();

""" RESULTADO (TERMINAL):

Digite sua senha: 123456
Usuário logado com sucesso!

Digite sua senha: 123
Senha incorreta!

"""

# 5. Escreva um programa que solicite ao usuário uma idade e verifique se ela está entre 18 e 30 anos (inclusive).
idade = int(input("Digite sua idade: "));

if (idade >= 18) and (idade <= 30):
    print("A idade está entre 18 e 30 anos");
else:
    print("A idade não está entre 18 e 30 anos");
    
print();

""" RESULTADO (TERMINAL):

Digite sua idade: 24
A idade está entre 18 e 30 anos

Digite sua idade: 50
A idade não está entre 18 e 30 anos

"""

# 6. Escreva um programa que solicite ao usuário três números inteiros e verifique se pelo menos um deles é positivo.
numero1 = int(input("Digite o primeiro número inteiro: "));
numero2 = int(input("Digite o segundo número inteiro: "));
numero3 = int(input("Digite o terceiro número inteiro: "));

if (numero1 > 0) or (numero2 > 0) or (numero3 > 0):
    print("Um dos números é positivo.");
else:
    print("Nenhum dos números é positivo.");
    
print();

""" RESULTADO (TERMINAL):

Digite o primeiro número inteiro: -7
Digite o segundo número inteiro: -2
Digite o terceiro número inteiro: -5
Nenhum dos números é positivo.

Digite o primeiro número inteiro: 54
Digite o segundo número inteiro: -78
Digite o terceiro número inteiro: -13
Um dos números é positivo.

"""

# 7. Escreva um programa que solicite ao usuário uma letra e verifique se ela é uma vogal (a, e, i, o, u).
letra = input("Digite uma letra: ");

if letra.lower() in ['a','e','i','o','u']:
    print("É uma vogal");
else:
    print("Não é vogal");

print();

""" RESULTADO (TERMINAL):

Digite uma letra: E
É uma vogal

Digite uma letra: V
Não é vogal

Digite uma letra: 3
Não é vogal

Digite uma letra: a
É uma vogal

"""

# 8. Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.
numero = int(input("Digite o primeiro número inteiro: "));

if numero > 0:
    print("O número é positivo.");
elif numero < 0:
    print("O número é negativo.");
else:
    print("O número é zero.");

print();

""" RESULTADO (TERMINAL):

Digite o primeiro número inteiro: 10
O número é positivo.

Digite o primeiro número inteiro: 0
O número é zero.

Digite o primeiro número inteiro: -4
O número é negativo.

"""

# 9. Escreva um programa que solicite ao usuário três números e verifique se eles estão em ordem crescente.
nume1 = float(input( "Digite 1º Número: "));
nume2 = float(input( "Digite 2º Número: "));
nume3 = float(input( "Digite 3º Número: "));

if (nume1 < nume2 < nume3):
    print("Os números estão em ordem crescente.");
else:
    print("Os números não estão em ordem crescente.");

print();

""" RESULTADO (TERMINAL):

Digite 1º Número: 3 
Digite 2º Número: 1
Digite 3º Número: 9
Os números não estão em ordem crescente.

Digite 1º Número: 12
Digite 2º Número: 15
Digite 3º Número: 20
Os números estão em ordem crescente.

Digite 1º Número: 4
Digite 2º Número: 8
Digite 3º Número: 0
Os números não estão em ordem crescente.

"""

# 10. Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é um múltiplo de 3 e 5 ao mesmo tempo.
numero4 = int(input("Digite um número inteiro: "));

if (numero4 % 3 == 0) and (numero4 % 5 == 0):
    print("O número é um múltiplo de 3 e 5 ao mesmo tempo.");
else:
    print("O número não é um múltiplo de 3 e 5 ao mesmo tempo.");

print();
    
""" RESULTADO (TERMINAL):

Digite um número inteiro: 8
O número não é um múltiplo de 3 e 5 ao mesmo tempo.

Digite um número inteiro: 0
O número é um múltiplo de 3 e 5 ao mesmo tempo.

Digite um número inteiro: 15
O número é um múltiplo de 3 e 5 ao mesmo tempo.

Digite um número inteiro: 5
O número não é um múltiplo de 3 e 5 ao mesmo tempo.

"""