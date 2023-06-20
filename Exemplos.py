# Exemplos 1

# 1. Solicite ao usuário que digite dois números e exiba a soma deles:
primeiroNumero = float(input("Digite o primeiro número: "));
segundoNumero = float(input("Digite o segundo número: "));

soma = primeiroNumero + segundoNumero

print("Valor da soma é ",soma);
print();

""" RESULTADO (TERMINAL)

Digite o primeiro número: 54.1
Digite o segundo número: 19.9
Valor da soma é  74.0

"""

# 2. Solicite ao usuário que digite um número e exiba se ele é par ou ímpar:
numero = int(input("Digite um número: "));

if numero % 2 == 0:
  print("Esse número é PAR.");
else:
    print("Esse número é IMPAR.");

print();

""" RESULTADO (TERMINAL)

Digite um número: 6
Esse número é PAR.

"""
     
# 3. Solicite ao usuário que digite uma temperatura em graus Celsius e converta-a para:
# A fórmula de conversão é: Fahremheit = Celsius * 9/5 + 32.

celsius = int(input("Digite a temperatura em Celsius para converter: "));
fahrenheit = (celsius * 9/5) + 32;

print("%s Celsius é igual Fahrenheit %s" % (celsius, int(fahrenheit)));
print();

""" RESULTADO (TERMINAL)

Digite a temperatura em Celsius para converter: 28
28 Celsius é igual Fahrenheit 82

"""

# 4. Solicite ao usuário que digite uma palavra e exiba quantas letras essa palavra contém:
palavra = input("Digite uma palavra: ");
quantidadedeLetras = len(palavra); #modelo len retorna a quantidade de letras em um texto

print("Quantidade de letras: ", quantidadedeLetras);
print();

"""  RESULTADO (TERMINAL)

Digite uma palavra: victor
Quantidade de letras: 6

"""

# 5. Exiba os números de 1 a 10 usando um loop:
for index in range(10):
  print(index + 1);

print();

"""  RESULTADO (TERMINAL)

1
2
3
4
5
6
7
8
9
10

"""

# 6. Escreva uma função em Python chamada "verificar_primo" que recebe um número como parâmetro e retorna True se o número for primo e False:
# Número primo somente é divisivel por ele e por 1
def verificar_primo(numero):
  if numero < 2:
    return False

  for divisor in range(2, int(numero / 2) + 1):
      if numero % divisor == 0:
        return False
  return True

numero = int(input("Digite um número: "))

if verificar_primo(numero):
  print("Esse número é impar");
else:
  print("Esse número NÃO é impar");

print();

""" RESULTADO (TERMINAL)

Digite um número: 65
Esse número NÃO é impar

"""
 
lista_alunos = ["João", "Carlos", "Ana", "Andre", "Lucas", "Livia"]

print("Mostre João");
print(lista_alunos[1]);
print();

""" RESULTADO (TERMINAL)

Mostre João
Carlos

"""

# 7. Quantos alunos eu tenho na lista:
quantidade_alunos = len(lista_alunos);
print(quantidade_alunos);
print();

""" RESULTADO (TERMINAL)

6

"""

# 8. Quero adicionar o Douglas:
lista_alunos.append("Douglas");
print(lista_alunos);
print();

""" RESULTADO (TERMINAL)

['João', 'Carlos', 'Ana', 'Andre', 'Lucas', 'Livia', 'Douglas']

"""

# 9. Quero remover o Andre:
lista_alunos.remove("Andre");
print(lista_alunos);
print();

""" RESULTADO (TERMINAL)

['João', 'Carlos', 'Ana', 'Lucas', 'Livia', 'Douglas']

"""

# 10. Limpar o minha lista de alunos:
lista_alunos.clear();
print(lista_alunos);
print();

""" RESULTADO (TERMINAL)

[]

"""

# 11. Quero verificar se o aluno João está na lista:
if "João" in lista_alunos:
  print("João está na lista");
else:
  print("Aluno não está na lista");

print();
  
""" RESULTADO (TERMINAL)

Aluno não está na lista

"""