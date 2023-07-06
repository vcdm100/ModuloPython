#Exemplo 1: contagem regressiva de 10 a 1

contador = 10;

while contador >= 1:
    print(contador);
    contador -= 1;

print();

""" RESULTADO (TERMINAL):

10
9
8
7
6
5
4
3
2
1

"""

#Exemplo 2: Leitura de notas de alunos até que uma nota negativa seja inserida

notas = [];

nota = float(input("Digite uma nota (-1 para sair): "));

while nota >= 0:
    notas.append(nota);
    nota = float(input("Digite uma nota (-1 para sair): "));
    
    if nota < -1:
        print("------------------------------------------------------------");
        print("Opção inválida, digite uma nota válida ou -1 para finalizar.");
        print("------------------------------------------------------------");
    
print(notas);
print();

""" RESULTADO (TERMINAL):

Digite uma nota (-1 para sair): 4.5
Digite uma nota (-1 para sair): 6.7
Digite uma nota (-1 para sair): 10.0
Digite uma nota (-1 para sair): 2.0
Digite uma nota (-1 para sair): 0.0
Digite uma nota (-1 para sair): -1
[4.5, 6.7, 10.0, 2.0, 0.0]

Digite uma nota (-1 para sair): 5.4
Digite uma nota (-1 para sair): 6.7
Digite uma nota (-1 para sair): 2.1
Digite uma nota (-1 para sair): -3
------------------------------------------------------------
Opção inválida, digite uma nota válida ou -1 para finalizar.
------------------------------------------------------------
[5.4, 6.7, 2.1]

"""

#Exemplo 3: Verificação de senha correta

senha = input("Informe uma senha: ");

contador = 0;
senhaBloqueada = False;

while senha != '123456' :
    print("Senha incorreta");
    contador += 1;
    if (contador == 3):
        senhaBloqueada = True;
        break;    
    senha = input("Digite a senha novamente: ");
    
if(senhaBloqueada):
    print("Sua senha foi bloqueada!");
else:
    print("Senha correta!");

print();

""" RESULTADO (TERMINAL):

Informe uma senha: 123
Senha incorreta
Digite a senha novamente: Vict@3$
Senha incorreta
Digite a senha novamente: Aos45
Senha incorreta
Sua senha foi bloqueada!

Informe uma senha: 112
Senha incorreta
Digite a senha novamente: 123456
Senha correta!

"""

#Exemplo 4: Impressão dos primeiros N numeros pares

quantidade = int(input("Informe a quantidade de numeros a serem impressos: "));

contador = 1;

while quantidade > 0 :
    if contador % 2 == 0:
        print(contador);
        quantidade -= 1;
    contador += 1;

print();

#Impares
quantidade = int(input("Informe a quantidade de numeros a serem impressos: "));

contador = 1;

while quantidade > 0 :
    if contador % 3 == 0:
        print(contador);
        quantidade -= 1;
    contador += 1;

print();

""" RESULTADO (TERMINAL):

Informe a quantidade de numeros a serem impressos: 5
2
4
6
8
10

Informe a quantidade de numeros a serem impressos: 4
3
6
9
12

"""

#Jogo da adivinhação

numeroSecreto = 42;
palpite = int(input("Digite um número: "));

while palpite != numeroSecreto:
    print("Você errou! Tente novamente")
    palpite = int(input("Digite um número: "));
    
print("Parabéns! Você acertou o palpite!");
print();

""" RESULTADO (TERMINAL):

Digite um número: 4
Você errou! Tente novamente
Digite um número: 5
Você errou! Tente novamente
Digite um número: 9
Você errou! Tente novamente
Digite um número: 67
Você errou! Tente novamente
Digite um número: 0
Você errou! Tente novamente
Digite um número: 42
Parabéns! Você acertou o palpite!

"""

#Exemplo 6: Impressão de uma sequência de caracteres até que a palavra "sair" seja digitada

palavra = input("Digite uma palavra ('sair' para encerrar): ");

palavra = palavra.lower();

while palavra != 'sair':
    print(palavra);
    palavra = input("Digite uma palavra ('sair' para encerrar): ");
    palavra = palavra.lower();

""" RESULTADO (TERMINAL):

Digite uma palavra ('sair' para encerrar): Victor
victor
Digite uma palavra ('sair' para encerrar): AULA
aula
Digite uma palavra ('sair' para encerrar): Python 
python
Digite uma palavra ('sair' para encerrar): SAIR

"""