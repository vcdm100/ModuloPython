# TESTE - jogo de adivinhação em Python:
import random

class Adivinhacao:

    def __init__(self, limite_inferior: int, limite_superior: int, max_tentativas: int ):
        
        self.limite_inferior = limite_inferior;
        self.limite_superior = limite_superior;
        self.max_tentativas = max_tentativas;
        self.numero_secreto = random.randint(self.limite_inferior, self.limite_superior);
        self.tentativas = 0;

    def iniciar_jogo(self):
        print();
        print(f"Bem-vindo ao jogo de adivinhação!");
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

    def jogar_novamente (self):
        jogar_novamente = input("Deseja jogar novamente? (Digite 's' para sim ou 'n' para não): ");
        print();

        if jogar_novamente.lower() == "s":
            self.__init__(self.limite_inferior, self.limite_superior, self.max_tentativas);
            self.iniciar_jogo();
        else:
            print("Obrigado por jogar!\n");