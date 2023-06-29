# Exercícios 02

# 1. Crie uma lista chamada "frutas" contendo as seguintes frutas: maçã, banana, laranja, abacaxi e melancia. Em seguida, exiba a lista completa na tela.
frutas = ["maçã", "banana", "laranja", "abacaxi", "melancia"]

print("Lista completa: ", frutas);
print();

""" RESULTADO (TERMINAL):

Lista completa:  ['maçã', 'banana', 'laranja', 'abacaxi', 'melancia']

"""

# 2. Adicione a fruta "uva" à lista "frutas" utilizando o método append(). Exiba a lista atualizada na tela.
frutas.append("uva")

print("Lista atualizada: ", frutas);
print();

""" RESULTADO (TERMINAL):

Lista atualizada:  ['maçã', 'banana', 'laranja', 'abacaxi', 'melancia', 'uva']

"""

# 3. Remova a fruta "banana" da lista "frutas" utilizando o método remove(). Exiba a lista atualizada na tela.
frutaRemovida = frutas.remove("banana");

print("Lista atualizada 2: ", frutas);
print();

""" RESULTADO (TERMINAL):

Lista atualizada 2:  ['maçã', 'laranja', 'abacaxi', 'melancia', 'uva']

"""

# 4. Acesse o segundo elemento da lista "frutas" e armazene-o em uma variável chamada "fruta_selecionada". Em seguida, exiba o valor armazenado na variável.
fruta_selecionada = frutas[1];

print("Segundo elemento da lista: ", fruta_selecionada);
print();

""" RESULTADO (TERMINAL):

Segundo elemento da lista:  laranja

"""

# 5. Crie uma tupla chamada "cores" contendo as seguintes cores: vermelho, azul, verde, amarelo e roxo. Em seguida, exiba a tupla completa na tela.
cores = ("vermelho", "azul", "verde", "amarelo", "roxo");

print("Tupla completa: ", cores);
print();

""" RESULTADO (TERMINAL):

Tupla completa:  ('vermelho', 'azul', 'verde', 'amarelo', 'roxo')

"""

# 6. Acesse o terceiro elemento da tupla "cores" e armazene-o em uma variável chamada "cor_selecionada". Em seguida, exiba o valor armazenado na variável.
cor_selecionada = cores[2];

print("Terceiro elemento da tupla: ", cor_selecionada);
print();

""" RESULTADO (TERMINAL):

Terceiro elemento da tupla:  verde

"""

# 7. Tente adicionar a cor "laranja" à tupla "cores" e observe o resultado. Explique o motivo pelo qual ocorreu um erro fazendo um comentário no código.
cores.append("laranja");

print("Cores: ", cores);
print();

""" RESULTADO (TERMINAL):

AttributeError: 'tuple' object has no attribute 'append'

    MOTIVO: Porque objeto "tupla" não tem um método "append()" para adicionar os elementos, por isso é imutável! 

"""

# 8. Crie um dicionário chamado "aluno" contendo as seguintes informações: nome, idade e cidade. Utilize as chaves "nome", "idade" e "cidade" para representar cada informação. Em seguida, exiba o dicionário completo na tela.
aluno = {
    "nome"   : "Victor",
    "idade"  : 24,
    "cidade" : "Recife"
}

print("Dicionário completo: ", aluno);
print();

""" RESULTADO (TERMINAL):

Dicionário completo:  {'nome': 'Victor', 'idade': 24, 'cidade': 'Recife'}

"""

# 9. Acesse a idade do aluno no dicionário "aluno" e armazene-o em uma variável chamada "idade_aluno". Em seguida, exiba o valor armazenado na variável.
idade_aluno = aluno["idade"];

print("Idade do aluno: ", idade_aluno);
print();

""" RESULTADO (TERMINAL):

Idade do aluno:  24

"""

# 10. Adicione a informação do gênero do aluno ao dicionário "aluno" utilizando a chave "gênero" e o valor correspondente. Exiba o dicionário atualizado na tela.
aluno["gênero"] = "Masculino";

print("Dicionário atualizado: ", aluno);
print();

""" RESULTADO (TERMINAL):

Dicionário atualizado:  {'nome': 'Victor', 'idade': 24, 'cidade': 'Recife', 'gênero': 'Masculino'}

"""

# 11. Remova a informação da cidade do dicionário "aluno" utilizando o método pop() e a chave correspondente. Exiba o dicionário atualizado na tela.
aluno.pop("cidade");

print("Dicionário atualizado 2: ", aluno);
print();

""" RESULTADO (TERMINAL):

Dicionário atualizado 2:  {'nome': 'Victor', 'idade': 24, 'gênero': 'Masculino'}

"""
