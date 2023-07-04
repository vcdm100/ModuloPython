#Exemplos de Estruturas Condicionais e Operadores Lógicos

#Verificação de idade para entrada em clube noturno:
idade = int(input("Digite sua idade: "));

if idade >= 18:
    print("Bem-vindo(a)(e), você pode entrar na festa!");
else:
    print("Desculpe, você não tem idade suficiente para entrar na festa.");
print();

""" RESULTADO (TERMINAL)

Digite sua idade: 24
Bem-vindo(a)(e), você pode entrar na festa!

Digite sua idade: 16
Desculpe, você não tem idade suficiente para entrar na festa.

"""
#Verificar se um número está dentro de um intervalo entre 10 e 20:
numero = 21;

if (numero >= 10) and (numero <= 20):
    print("O número está dentro do intervalo");
else:
    print("O número está fora do intervalo");
print();

""" RESULTADO (TERMINAL)

O número está fora do intervalo

"""

# 1. Comparar o tamanho de duas listas:
lista1 = [1,2,3,4,5];
lista2 = [5,4,3,2,'a'];

if len(lista1) > len(lista2):
    print("A lista 1 é maior que a lista2");
elif len(lista1) < len(lista2):
    print("A lista 2 é maior que a 1");
else:
    print("As listas tem mesmo tamanho");
print();
    
""" RESULTADO (TERMINAL)

As listas tem mesmo tamanho

"""

# 2. Comparar o tamanho de outras duas listas:
lista11 = [1,2,3,4,5];
lista22 = [5,4,3,2,'a',7,"Victor",True];

if len(lista11) > len(lista22):
    print("A lista 11 é maior que a lista22");
elif len(lista11) < len(lista22):
    print("A lista 22 é maior que a 11");
else:
    print("As listas tem mesmo tamanho");
print();
    
""" RESULTADO (TERMINAL)

A lista 22 é maior que a 11

"""

# 3. Comparar o tamanho de outras mais duas listas:
lista111 = [1,2,3,4,5,6,7];
lista222 = [5,4,3,2,'a'];

if len(lista111) > len(lista222):
    print("A lista 111 é maior que a lista222");
elif len(lista111) < len(lista222):
    print("A lista 222 é maior que a 111");
else:
    print("As listas tem mesmo tamanho");
print();
    
""" RESULTADO (TERMINAL)

A lista 111 é maior que a lista222

"""

#Verificação de acesso um sistema:
senha = input("Digite sua senha: ");

senha_correta = "1998@Victor";

if senha == senha_correta:
    print("Usuário logado com sucesso!");
else:
    print("A senha informada está errada!");
print();

""" RESULTADO (TERMINAL)

Digite sua senha: 1998@Victor
Usuário logado com sucesso!

Digite sua senha: 1924@Victor
A senha informada está errada!

"""

#Verificação de acesso um sistema com login e senha
usuario = input("Digite o seu usuário: ");
senha = input("Digite sua senha: ");

usuarioCorreto  = "admin";
senhaCorreta    = "admin";

if (usuario != usuarioCorreto) and (senha != senhaCorreta):
    print("Usuário e senha incorretos!");
if usuario != usuarioCorreto:
    print("O usuário está incorreto!");
elif not(senha == senhaCorreta):
    print("A senha está incorreta!");
else:
    print("Login bem-sucedido!");

print();

""" RESULTADO (TERMINAL)

Digite o seu usuário: admin
Digite sua senha: admin
Login bem-sucedido!

Digite o seu usuário: admin
Digite sua senha: adm41
A senha está incorreta!

Digite o seu usuário: 45
Digite sua senha: admin
O usuário está incorreto!

"""

#Verifica de múltiplas condiçôes com "and" ou "or":
numero = 10;

if (numero > 0 and numero < 5) or (numero > 10 and numero < 15):
    print("O número atende aos critérios");
else:
    print("O número não atende os critérios");

print();

""" RESULTADO (TERMINAL)

O número não atende os critérios

"""

#Verificação de uma condição negada
#Verificar se uma pessoa está apta a dirigir

idade = int(input("Informe sua idade: "));
possuiCarteira = False;

if idade >= 18 and not possuiCarteira:
    print("Você precisa de ter a carteira de motorista!");
else:
    print("Você está apto a dirigir!");

print();

""" RESULTADO (TERMINAL)

Informe sua idade: 24
Você precisa de ter a carteira de motorista!

Informe sua idade: 17
Você está apto a dirigir!

"""

#MATCH CASE
comando = 'Olá, mundo!'

match comando:
    case 'Olá, mundo!':
        print("Olá para você também");
    case 'Adeus, Mundo':
        print("Adeus!");
    case _:
        print("Sem resultados!");
        
""" RESULTADO (TERMINAL)

Olá para você também

"""