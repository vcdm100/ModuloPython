listaNumeros = [1, 2, 3, 4, 5];
listaStrings = ["a", "b", "c", "d"];
listaMista = [1, "a", 3.14, True];

print(listaNumeros);
print(listaStrings);
print(listaMista);
print();

frutas = ["maça", "banana", "morango"];

print("gosto de comer da", frutas[1]);
print();

frutas[1] = "laranja";

print(frutas);
print("Tamanho 1: ", len(frutas));
print();

frutas.append("abacaxi");

print(frutas);
print("Tamanho 2: ", len(frutas));
print();

listaNova = [1, ["a", "b"]];

print(listaNova[1][0]);
print();

lista1 = [1,2,3];
lista2 = [4,5,6];

lisa_concatenada = lista1 + lista2;

print(lisa_concatenada);
print();

listaRepetida = [0] * 3;

print(listaRepetida);
print();

numeros = [1,2,3,4];
numeros2 = ["a", "b", "c", "d"];

sublista = numeros[1:4];
sublista2 = numeros2[2:4];

print(sublista);
print(sublista2);
print();

""" RESULTADO (TERMINAL)

[1, 2, 3, 4, 5]
['a', 'b', 'c', 'd']
[1, 'a', 3.14, True]

gosto de comer da banana

['maça', 'laranja', 'morango']
Tamanho 1:  3

['maça', 'laranja', 'morango', 'abacaxi']
Tamanho 2:  4

a

[1, 2, 3, 4, 5, 6]

[0, 0, 0]

[2, 3, 4]
['c', 'd']

"""