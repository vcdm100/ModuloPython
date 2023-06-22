#Exemplos de programa que aborda o tipo de dado string em Python

frase = "Olá, sou Victor Cláudio!"

#Declaração de uma String
print("String original: ");
print(frase);
print();

#Acessando caracteres individuais
print("Acessando caracteres individuais: ");
print("Frase: ", frase);
print("Primeiro caractere: ", frase[0]);
print("Segundo caractere: ", frase[1]);
print("Último caractere: ", frase[-1]);
print("PenÚltimo caractere: ", frase[-2]);
print();

#Mais um exemplo
s = "banana";
vc = 'Victor';

print(s, id(s));
print();

#Exemplo de troca uma letra da palavra

vcs = vc.replace("V", "B");

print(vcs); #ou print(vc.replace("V", "B"));
print();

#Utilizando o input para pegar um nome informado pelo usuário:
nome = input("Nome: ");

print(nome);
print();

#Inserindo as variáveis no print com f
print(f"Bem-vindo, {nome}");
print(f"Bem-vindo, {7*3}");
print("Bem-vindo, {}".format(nome));
print();

#Concatenando strings
print("Concatenando strings: ");

outraFrase = "Bem-vindo";
fraseCompleta = frase + ' ' + outraFrase;

print(fraseCompleta);
print();

#Tamanho da string 
tamanho = len(frase);

print("Tamanho: ", tamanho);
print();

#Divindo uma string em sub strings
print("Divindo a string: ");

palavras = fraseCompleta.split();

print(palavras);
print();

#Substituindo parte das strings
print("Substituindo parte das strings: ");

novaFrase = frase.replace("Cláudio", "Python");

print(novaFrase);
print();

#Convertendo para letras maiúsculas e minúsculas
print("Convertendo para letras maiúsculas e minúsculas: ");

print("Maiúsculas: ", frase.upper());
print("Minúsculas: ", frase.lower());
print();

""" RESULTADO (TERMINAL):

String original: 
Olá, sou Victor Cláudio!

Acessando caracteres individuais:
Frase:  Olá, sou Victor Cláudio!
Primeiro caractere:  O
Segundo caractere:  l
Último caractere:  !
PenÚltimo caractere:  o

banana 2408880350704

Bictor

Nome: Vinicius 
Vinicius

Bem-vindo, Vinicius
Bem-vindo, 21
Bem-vindo, Vinicius

Concatenando strings:
Olá, sou Victor Cláudio! Bem-vindo

Tamanho:  24

Divindo a string:
['Olá,', 'sou', 'Victor', 'Cláudio!', 'Bem-vindo']

Substituindo parte das strings:
Olá, sou Victor Python!

Convertendo para letras maiúsculas e minúsculas:
Maiúsculas:  OLÁ, SOU VICTOR CLÁUDIO!
Minúsculas:  olá, sou victor cláudio!

"""