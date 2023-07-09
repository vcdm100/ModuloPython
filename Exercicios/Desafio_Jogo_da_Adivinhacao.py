# Neste jogo de desafio, o computador vai escolher um número aleatório e o jogador deve tentar adivinhar qual é esse número. O computador irá fornecer dicas dizendo se o palpite do jogador está acima ou abaixo do número correto.

# PROPOSTA: Melhorias na versão inicial do jogo: 
    # 1. Adicionar limite máximo de tentativas; (feito)
    # 2. Permitir que o jogador escolha o intervalo de números; (feito)
    # 3.  Incluir uma opção para o jogador jogar novamente ou sair do jogo após acertar ou esgotar todas as tentativas. (feito)

# DICAS: Criar 3 novas variáveis: “limite_inferior”, “limite_superior” e “max_tentativas”. Ao final do jogo, se o jogador acertar ou esgotar todas as tentativas, o programa pergunta se o jogador deseja jogar novamente.

import random

def adivinhacao():
    
    nome = input("Nome de Jogador: ").lower();
    print();
    limite_inferior = int(input("Escolha o número mínimo de intervalos: "));
    limite_superior = int(input("Escolha o número máximo de intervalos: "));
    max_tentativas = int(input("Quantidade máxima de tentativas: "));
    
    # Gera um número aleatório entre (limite_inferior como 1) e (limite_superior como 100).
    numero_secreto = random.randint(limite_inferior, limite_superior);  

    tentativas = 0;

    print();
    print(f"Bem-vindo ao jogo de adivinhação, {nome}!");
    print(f"Estou pensando em um número entre {limite_inferior} e {limite_superior}.", "\n");

    while tentativas < max_tentativas:
        
        palpite = int(input("Digite o seu palpite: "));
        tentativas += 1;

        if palpite < numero_secreto:
            contador = max_tentativas - tentativas;
            print(f"Tente um número maior! Você possui {contador} de total {max_tentativas} tentativas."); 
        elif palpite > numero_secreto:
            contador = max_tentativas - tentativas;
            print(f"Tente um número menor! Você possui {contador} de total {max_tentativas} tentativas.");
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!");
            break
        print();
        
    if tentativas == max_tentativas:
        print(f"Fim do jogo!");
        print(f"O número correto era {numero_secreto}. Você esgotou todas as tentativas.");

    jogar_novamente = input("Deseja jogar novamente? (Digite 's' para sim ou 'n' para não): ");
    print();
    
    if jogar_novamente.lower() == "s":
        adivinhacao();
    else:
        print("Obrigado por jogar!", "\n");

adivinhacao();

""" RESULTADO (TERMINAL):

Nome de Jogador: VictOR

Escolha o número mínimo de intervalos: 1
Escolha o número máximo de intervalos: 100
Quantidade máxima de tentativas: 10

Bem-vindo ao jogo de adivinhação, victor!
Estou pensando em um número entre 1 e 100. 

Digite o seu palpite: 25
Tente um número maior! Você possui 9 de total 10 tentativas.

Digite o seu palpite: 95
Tente um número menor! Você possui 8 de total 10 tentativas.

Digite o seu palpite: 76
Tente um número menor! Você possui 7 de total 10 tentativas.

Digite o seu palpite: 38
Tente um número maior! Você possui 6 de total 10 tentativas.

Digite o seu palpite: 62
Tente um número menor! Você possui 5 de total 10 tentativas.

Digite o seu palpite: 44
Tente um número menor! Você possui 4 de total 10 tentativas.

Digite o seu palpite: 39
Parabéns! Você acertou o número em 7 tentativas!
Deseja jogar novamente? (Digite 's' para sim ou 'n' para não): S

Nome de Jogador: CLÁUDIO

Escolha o número mínimo de intervalos: 25
Escolha o número máximo de intervalos: 50
Quantidade máxima de tentativas: 5

Bem-vindo ao jogo de adivinhação, cláudio!
Estou pensando em um número entre 25 e 50.

Digite o seu palpite: 47
Tente um número menor! Você possui 4 de total 5 tentativas.

Digite o seu palpite: 28
Tente um número maior! Você possui 3 de total 5 tentativas.

Digite o seu palpite: 32
Tente um número maior! Você possui 2 de total 5 tentativas.

Digite o seu palpite: 41
Tente um número menor! Você possui 1 de total 5 tentativas.

Digite o seu palpite: 37
Tente um número maior! Você possui 0 de total 5 tentativas.

Fim do jogo!
O número correto era 39. Você esgotou todas as tentativas.
Deseja jogar novamente? (Digite 's' para sim ou 'n' para não): n

Obrigado por jogar!

"""