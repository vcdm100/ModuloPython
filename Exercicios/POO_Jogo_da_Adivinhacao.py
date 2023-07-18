# Código do jogo de adivinhação em Python para usar Programação Orientada a Objetos (POO):
import random

class Adivinhacao:

    def __init__(self):
        self.nome = input("Nome de Jogador: ").lower();
        self.limite_inferior = int(input("Escolha o número mínimo de intervalos: "));
        self.limite_superior = int(input("Escolha o número máximo de intervalos: "));
        self.max_tentativas = int(input("Quantidade máxima de tentativas: "));
        self.numero_secreto = random.randint(self.limite_inferior, self.limite_superior);
        self.tentativas = 0;

    def iniciar_jogo(self):
        print();
        print(f"Bem-vindo ao jogo de adivinhação, {self.nome}!");
        print(f"Estou pensando em um número entre {self.limite_inferior} e {self.limite_superior}.\n");

        while self.tentativas < self.max_tentativas:
            palpite = int(input("Digite o seu palpite: "));
            self.tentativas += 1;

            if palpite < self.numero_secreto:
                contador = self.max_tentativas - self.tentativas;
                print(f"Tente um número maior! Você possui {contador} de total {self.max_tentativas} tentativas.");
            elif palpite > self.numero_secreto:
                contador = self.max_tentativas - self.tentativas;
                print(f"Tente um número menor! Você possui {contador} de total {self.max_tentativas} tentativas.");
            else:
                print(f"Parabéns! Você acertou o número em {self.tentativas} tentativas!");
                break
            print()

        if self.tentativas == self.max_tentativas:
            print("Fim do jogo!");
            print(f"O número correto era {self.numero_secreto}. Você esgotou todas as tentativas.");

        jogar_novamente = input("Deseja jogar novamente? (Digite 's' para sim ou 'n' para não): ");
        print();

        if jogar_novamente.lower() == "s":
            self.__init__();
            self.iniciar_jogo();
        else:
            print("Obrigado por jogar!\n");

jogo = Adivinhacao();
jogo.iniciar_jogo();

""" RESULTADO (TERMINAL):

Nome de Jogador: VIctOR
Escolha o número mínimo de intervalos: 1
Escolha o número máximo de intervalos: 60
Quantidade máxima de tentativas: 9

Bem-vindo ao jogo de adivinhação, victor!
Estou pensando em um número entre 1 e 60.

Digite o seu palpite: 55
Tente um número menor! Você possui 8 de total 9 tentativas.

Digite o seu palpite: 20
Tente um número maior! Você possui 7 de total 9 tentativas.

Digite o seu palpite: 30
Tente um número menor! Você possui 6 de total 9 tentativas.

Digite o seu palpite: 22
Tente um número maior! Você possui 5 de total 9 tentativas.

Digite o seu palpite: 28
Tente um número menor! Você possui 4 de total 9 tentativas.

Digite o seu palpite: 25
Tente um número maior! Você possui 3 de total 9 tentativas.

Digite o seu palpite: 26
Parabéns! Você acertou o número em 7 tentativas!
Deseja jogar novamente? (Digite 's' para sim ou 'n' para não): S

Nome de Jogador: brUNA
Escolha o número mínimo de intervalos: 1  
Escolha o número máximo de intervalos: 25
Quantidade máxima de tentativas: 3

Bem-vindo ao jogo de adivinhação, bruna!
Estou pensando em um número entre 1 e 25.

Digite o seu palpite: 2
Tente um número maior! Você possui 2 de total 3 tentativas.

Digite o seu palpite: 24
Tente um número menor! Você possui 1 de total 3 tentativas.

Digite o seu palpite: 15
Tente um número menor! Você possui 0 de total 3 tentativas.

Fim do jogo!
O número correto era 8. Você esgotou todas as tentativas.
Deseja jogar novamente? (Digite 's' para sim ou 'n' para não): n

Obrigado por jogar!

"""