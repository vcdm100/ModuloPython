# #Exemplo 1: contagem regressiva de 10 a 1

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

#Exemplo 5: Jogo da adivinhação

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

# Exemplo 7: Implementação de menu  opções.

opcao = 0;

while opcao != 4:
    print("Menu: ")
    print("1. Opção 1");
    print("2. Opção 2");
    print("3. Opção 3");
    print("4. Sair");
    
    opcao = int(input("Informe a opção escolihda: "));
    
    if opcao == 1:
        print("Opção 1 selecionada!");
    elif opcao == 2:
        print("Opção 2 selecionada!");
    elif opcao == 3:
        print("Opção 3 selecionada!");
    elif opcao == 4:
        print("Saindo...");
    else:
        print("Opção inválida, tente novamente")

print();

""" RESULTADO (TERMINAL):

Menu: 
1. Opção 1
2. Opção 2
3. Opção 3
4. Sair
Informe a opção escolihda: 1
Opção 1 selecionada!
Menu: 
1. Opção 1
2. Opção 2
3. Opção 3
4. Sair
Informe a opção escolihda: 5
Opção inválida, tente novamente
Menu:
1. Opção 1
2. Opção 2
3. Opção 3
4. Sair
Informe a opção escolihda: 3
Opção 3 selecionada!
Menu:
1. Opção 1
2. Opção 2
3. Opção 3
4. Sair
Informe a opção escolihda: 4
Saindo...

"""

#Exemplo 8: EMULANDO DO WHILE

palavraSecreta = "python";
contador = 0;

while True:
    
    palavra = input("Informe a palavra secreta: ").lower();
    contador += 1;
    
    if palavra == palavraSecreta:
        print("Você acertou a palavra secreta!");
        break;
    
    if palavra != palavraSecreta:
        
        tentativas = 7 - contador;
        
        print(f"Palavra errada! Você possui {tentativas} de total 7 tentativas");
    
    if (palavra != palavraSecreta and contador >= 7):
        print("Você atingiu o limite de tentativas!");
        break;

print();

""" RESULTADO (TERMINAL):

Informe a palavra secreta: Oi
Palavra errada! Você possui 6 de total 7 tentativas
Informe a palavra secreta: METODOLGIA
Palavra errada! Você possui 5 de total 7 tentativas
Informe a palavra secreta: ÁGUA
Palavra errada! Você possui 4 de total 7 tentativas
Informe a palavra secreta: PYTHon
Você acertou a palavra secreta!

Informe a palavra secreta: Simone
Palavra errada! Você possui 6 de total 7 tentativas
Informe a palavra secreta: Victor
Palavra errada! Você possui 5 de total 7 tentativas
Informe a palavra secreta: Data
Palavra errada! Você possui 4 de total 7 tentativas
Informe a palavra secreta: Bruna
Palavra errada! Você possui 3 de total 7 tentativas
Informe a palavra secreta: Aula
Palavra errada! Você possui 2 de total 7 tentativas
Informe a palavra secreta: Prova
Palavra errada! Você possui 1 de total 7 tentativas
Informe a palavra secreta: PHP
Palavra errada! Você possui 0 de total 7 tentativas
Você atingiu o limite de tentativas!

"""