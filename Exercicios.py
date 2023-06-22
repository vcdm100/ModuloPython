# Exercícios 01

# 1. Crie duas variáveis, nome e idade, e atribua a elas seus próprios valores. Em seguida, use a formatação de strings para imprimir a seguinte mensagem: "Olá, meu nome é [nome] e eu tenho [idade] anos."
nome = "Victor Cláudio";
idade = 24;

print("Olá, meu nome é {} e eu tenho {} anos.".format(nome, idade));
print();

""" RESULTADO (TERMINAL):

Olá, meu nome é Victor Cláudio e eu tenho 24 anos.

"""

# 2. Crie uma variável chamada frase e atribua a ela uma string. Em seguida, use a função len() para imprimir o comprimento da frase.
frase = "Me formei no Curso Superior de graduação - Bacharelado em Engenharia Civil por Universidade Católica de Pernambuco."

comprimento = len(frase);

print("O comprimento da frase: ", comprimento);
print();

""" RESULTADO (TERMINAL):

O comprimento da frase:  115

"""

# 3. Crie duas variáveis, nome e sobrenome, e atribua a elas seus próprios valores. Concatene as variáveis para criar uma nova variável chamada nome_completo e imprima o resultado.
nome2 = "Victor Cláudio";
sobrenome = "Deosdede Moura";

nome_completo = nome2 + ' ' + sobrenome;

print("Nome completo: ", nome_completo);
print();

""" RESULTADO (TERMINAL):

Nome completo:  Victor Cláudio Deosdede Moura

"""

# 4. Crie uma variável chamada frase e atribua a ela uma string. Use o método upper() para imprimir a frase em letras maiúsculas.
frase2 = "Deficiente Auditivo Bilateral e/ou Surdo."

print("Maiúsculas: ", frase2.upper());
print();

""" RESULTADO (TERMINAL):

Maiúsculas:  DEFICIENTE AUDITIVO BILATERAL E/OU SURDO.

"""

# 5. Crie uma variável chamada frase e atribua a ela uma string contendo uma frase completa. Use o método split() para dividir a frase em uma lista de palavras e imprima o resultado.
frase3 = "Atualmente estou cursando a segunda graduação de Tecnólogo em Análise e Desenvolvimento de Sistemas (ADS)."

palavras = frase3.split();

print("Lista de palavras: ", palavras);
print();

""" RESULTADO (TERMINAL):

Lista de palavras:  ['Atualmente', 'estou', 'cursando', 'a', 'segunda', 'graduação', 'de', 'Tecnólogo', 'em', 'Análise', 'e', 'Desenvolvimento', 'de', 'Sistemas', '(ADS).']

"""

# 6. Crie uma variável chamada frase e atribua a ela uma string. Use o método replace() para substituir uma palavra específica na frase por outra palavra de sua escolha. Imprima a frase modificada.
frase4 = "Possuo alguns certificados de cursos complementares."

fraseModificada = frase4.replace("alguns", "os");

print(fraseModificada);
print();

""" RESULTADO (TERMINAL):

Possuo os certificados de cursos complementares.

"""

# 7. Crie duas váriaveis, “numero1” e “numero2” e atribua valores númerico a elas, depois crie uma váriavel resultado e armazene o resultado da soma das váriaveis “numero1” e “numero2”. Ao final imprima o resultado.
numero1 = 45;
numero2 = 8;

soma = numero1 + numero2;

print("Resultado: ", soma);
print();

""" RESULTADO (TERMINAL):

Resultado:  53

"""

# 8. Escreva um programa que solicite ao usuário que digite dois números inteiros e exiba a multiplicação desses números.
num1 = int(input("Digite o primeiro número: "));
num2 = int(input("Digite o segundo número: "));

mult = num1 * num2;

print("Valor da multiplicação: ", mult);
print();

""" RESULTADO (TERMINAL):

Digite o primeiro número: 32
Digite o segundo número: 9
Valor da multiplicação:  288

"""