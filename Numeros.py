#Exemplo de programa que aborda o tipo de dado númerico em Python

#Operações matemáticas básicas
num1 = 30;
num2 = 6;

soma            = num1 + num2;
subtracao       = num1 - num2;
multiplicacao   = num1 * num2;
divisao         = num1 / num2;
resto           = num1 % num2;
potencia        = num1 ** num2;

print("Operações matemáticas básicas: ");
print("Soma: ", soma);
print("Subtração: ", subtracao);
print("Multiplicação: ", multiplicacao);
print("Divisão: ", divisao);
print("Resto: ", resto);
print("Potência: ", potencia);
print();

#Arredondamento de número
numeroFloat = 3.144566565646;

numeroArredondado = round(numeroFloat);

print("Arredondamento: ", numeroArredondado);
print();

#Funções matemáticas da biblioteca "math"
import math

num = 4.7;

print("Funções matemáticas: ");
print("Valor absoluto: ", abs(-4.7));
print("Arredondamento para cima: ", math.ceil(num));
print("Arredondamento para baixo: ", math.floor(num));
print();

#Geração números aleatórios
import random

print("Números aleatórios: ");
print("Números aleatórios de 1 a 10: ", random.randint(1, 10));
print("Número float aleatório entre 0 e 1: ", random.random());
print();

#Formatação de números
numeroFormatado = 1234.567891098;

print("Formatação de números: ");
print(f"Número com 4 casas decimais: {numeroFormatado:.4f}");
print("Número formatado com 2 casas decimais: {:.2f}".format(numeroFormatado));
print();

""" RESULTADO (TERMINAL)

Operações matemáticas básicas: 
Soma:  36
Subtração:  24
Multiplicação:  180
Divisão:  5.0
Resto:  0
Potência:  729000000

Arredondamento:  3

Funções matemáticas: 
Valor absoluto:  4.7
Arredondamento para cima:  5
Arredondamento para baixo:  4

Números aleatórios:
Números aleatórios de 1 a 10:  4
Número float aleatório entre 0 e 1:  0.036379538931144095

Formatação de números:
Número com 4 casas decimais: 1234.5679
Número formatado com 2 casas decimais: 1234.57

"""