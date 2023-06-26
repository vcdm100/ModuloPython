#Exemplos de declaração de listas
listaNumeros = [1, 2, 3, 4, 5];
listaStrings = ["a", "b", "c", "d"];
listaMista = [1, "a", 3.14, True];

print(listaNumeros);
print(listaStrings);
print(listaMista);
print();

#ACESSANDO A LISTA POR INDICES
frutas = ["maça", "banana", "morango"];

print("gosto de comer da", frutas[1]);
print();

#ALTERANDO UM ITEM ESPECIFÍCO DA LISTA
frutas[1] = "laranja";

print(frutas);
#IMPRIMINDO O TAMANHO DA LISTA
print("Tamanho 1: ", len(frutas));
print();

#ADICIONANDO UM ITEM AO FINAL DA LISTA
frutas.append("abacaxi");

print(frutas);
print();

#INSERINDO UM ITEM EM UM INDÍCE ESPECÍFICO DA LISTA
frutas.insert(0,"uva");

print(frutas);
#IMPRIMINDO O TAMANHO DA LISTA
print("Tamanho 2: ", len(frutas));
print();

#REMOVENDO UM ITEM DA LISTA COM O METODO REMOVE
frutaRemovida = frutas.remove("morango");
#REMOVENDO UM ITEM DA LISTA COM O METODO POP
frutaRemovida = frutas.pop(2);

print(frutas);
print(frutaRemovida);
print();

#ORDENANDO UMA LISTA
frutas.sort();

print("Ordenando: ", frutas);
print();

#ACESSANDO SUBLISTAS
listaNova = [1, ["a", "b"]];

print(listaNova[1][0]);
print();

#CONCATENANDO LISTAS
lista1 = [1,2,3];
lista2 = [4,5,6];

lisa_concatenada = lista1 + lista2;

print(lisa_concatenada);
print();

#DECLARANDO UM VALOR REPETIDO NAS LISTAS
listaRepetida = [0] * 3;

print(listaRepetida);
print();

#FATIAMENTO DE LISTAS
numeros = [1,2,3,4];
numeros2 = ["a", "b", "c", "d"];

sublista = numeros[1:4];
sublista2 = numeros2[2:4];

print(sublista);
print(sublista2);
print();

#EMBARALHANDO UMA LISTA
from random import shuffle

shuffle(frutas);

print("Embaralhado: ", frutas);
print();

""" RESULTADO (TERMINAL)

[1, 2, 3, 4, 5]
['a', 'b', 'c', 'd']
[1, 'a', 3.14, True]

gosto de comer da banana

['maça', 'laranja', 'morango']
Tamanho 1:  3

['maça', 'laranja', 'morango', 'abacaxi']

['uva', 'maça', 'laranja', 'morango', 'abacaxi']
Tamanho 2:  5

['uva', 'maça', 'abacaxi']
laranja

Ordenando:  ['abacaxi', 'maça', 'uva']

a

[1, 2, 3, 4, 5, 6]

[0, 0, 0]

[2, 3, 4]
['c', 'd']

Embaralhado:  ['maça', 'abacaxi', 'uva']

"""