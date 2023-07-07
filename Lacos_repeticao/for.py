# #Exemplo 1: Impressão números 1 a 10

for numero in range(1, 11):
    print(numero);

print();

""" RESULTADO (TERMINAL):

1
2
3
4
5
6
7
8
9
10

"""

#Exemplo 2: Impressão de frutas de uma lista de frutas

frutas = ["maça", "uva", "Limão", "laranja", "Banana"];

for nome in frutas:
    print(nome);

print();

""" RESULTADO (TERMINAL):

maça
uva
Limão
laranja
Banana

"""

# Exemplo 2.1;

for nome in frutas:
    if nome == "laranja":
        continue;
    print(nome);

print();

""" RESULTADO (TERMINAL):

maça
uva
Limão
Banana

"""

# Exemplo 2.2;

for nome in frutas:
    if (nome == "laranja"):
        print("Encontrou laranja!");
        break;
    print(nome);

print();

""" RESULTADO (TERMINAL):

maça
uva
Limão
Encontrou laranja!

"""

#Exemplo 3: Cálculo da média de uma lista de notas

notas = [7.5, 8.0, 6.5, 9.0, 7.0];

soma = 0;

for nota in notas:
    soma += nota;

media = soma / len(notas);

print("A média é: ", media);
print();

""" RESULTADO (TERMINAL):

A média é:  7.6

"""

#Exemplo 4: Contando as vogais de uma string

palavra = "python-ae";
vogais = 0;

for letra in palavra:
    if letra in "aeiou":
        vogais += 1;

print(f"A palavra {palavra} possui {vogais} vogal.");
print();

""" RESULTADO (TERMINAL):

A palavra python-ae possui 3 vogal.

"""

# Exemplo 5: Iteração sobre os itens de uma lista

lista = ["a", "b", "c", "d", "e"];

for indice in range(len(lista)):
    if indice == 0:
        lista[indice] = "z";
    print(f"O elemento no indice {indice} é {lista[indice]}");

print();

""" RESULTADO (TERMINAL):

O elemento no indice 0 é z
O elemento no indice 1 é b
O elemento no indice 2 é c
O elemento no indice 3 é d
O elemento no indice 4 é e

"""

# Exemplo 6: Iteração sobre um elemento número com incremento

for numero in range(1, 21, 3):
    print(numero);
print();

for numero in range(2, 11, 2):
    print(numero);
print();

for numero in range(5, 21, 5):
    print(numero);
print();

""" RESULTADO (TERMINAL):

1
4
7
10
13
16
19

2
4
6
8
10

5
10
15
20

"""