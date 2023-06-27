#Exemplos de declaração de tuplas
tupla1 = (1,2,3,4,5,6);
tupla2 = ("a", "b", "c","d","e","f");
tupla3 = (1,"Olá", True);
tupla4 = 1,2,3,4;

print(tupla1);
print(tupla2);
print(type(tupla3));
print(type(tupla4));
print();

#ACESSANDO ITENS INDIVIDUALMENTE EM TUPLAS
print(tupla2[1]);
print();

#EXEMPLO DE UMA FORMA ERRADA DE ACESSAR UM ITEM DA TUPLA
# print(tupla2(2));

#CONCEITO PRINCIPAL DE TUPLAS: "IMUTÁVEL!"
# tupla2[1] = "g";

#FATIAMENTO DE ITENS NA TUPLA
print(tupla1[1:4]);
print();

#CONCATENANDO TUPLAS
tupla5 = 1,2,3;
tupla6 = 4,5,6;

tupla7 = tupla5 + tupla6;

print("Concatenando tuplas: ",tupla7);
print();

#CRIANDO VARIAVEIS NOVAS COM OS VALORES DE UMA TUPLA
a, b, c = tupla6;

a = tupla5[1];
b = tupla3[2];

print("Valores das variáveis: ");
print(a);
print(b);
print(c);
print();

""" RESULTADO (TERMINAL)

(1, 2, 3, 4, 5, 6)
('a', 'b', 'c', 'd', 'e', 'f')
<class 'tuple'>
<class 'tuple'>

b

(2, 3, 4)

Concatenando tuplas:  (1, 2, 3, 4, 5, 6)

Valores das variáveis: 
2
True
6

"""