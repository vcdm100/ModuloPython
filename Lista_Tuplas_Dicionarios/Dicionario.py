meuDicionario = {
    "nome"      : "Victor",
    "sobrenome" : "Moura",
    "apelido"   : "Vitão",
    "idade"     : 24,
    "chave"     : "valor"
}
print(meuDicionario);
print();

frutaDicionario = {
    'maçã'   : 3,
    'banana' : 6,
    'uva'    : 8,
    'vitaminas' : {'a' : 'boa para pele'}
};

print("Significado encontrado no dicionário: ",
      frutaDicionario["uva"]);
print();
print(frutaDicionario["vitaminas"]["a"]);
print();
print("Quantidade de maçãs: ", frutaDicionario.get("maçã"));
print("Quantidade de bananas: ", frutaDicionario.get("banana"));
print();
print("Chaves encontradas no dicionário: ", frutaDicionario.keys());
print("Valores encontrados no dicionário: ", frutaDicionario.values());
print("items encontrados no dicionário: ", frutaDicionario.items());
print();
print("Quantidade de morangos: ", frutaDicionario.get("morangos", "Não foi encontrado a definição de morango"));
print();

elementoRemovido = frutaDicionario.pop("uva");
print(elementoRemovido);
print();
print("Dicionário atualizado: ", frutaDicionario);
print();

frutaDicionario["maçã"] = 5;

print("Nova quantidade de maçã: ", frutaDicionario["maçã"]);
print();

frutaDicionario["laranja"] = 10;

print(frutaDicionario);
print();

animaisDicionario = {};
animaisDicionario["cachorro"] = "Batolomeu";

print(animaisDicionario);
print();

aluno = {
    'nome' : 'Victor',
    'idade' : 24,
    'hobbies' : ['jogar xadrez', 'esportes']
}

print(aluno);
print();

""" RESULTADO (TERMINAL)

{'nome': 'Victor', 'sobrenome': 'Moura', 'apelido': 'Vitão', 'idade': 24, 'chave': 'valor'}

Significado encontrado no dicionário:  8

boa para pele

Quantidade de maçãs:  3
Quantidade de bananas:  6

Chaves encontradas no dicionário:  dict_keys(['maçã', 'banana', 'uva', 'vitaminas'])
Valores encontrados no dicionário:  dict_values([3, 6, 8, {'a': 'boa para pele'}])
items encontrados no dicionário:  dict_items([('maçã', 3), ('banana', 6), ('uva', 8), ('vitaminas', {'a': 'boa para pele'})])

Quantidade de morangos:  Não foi encontrado a definição de morango

8

Dicionário atualizado:  {'maçã': 3, 'banana': 6, 'vitaminas': {'a': 'boa para pele'}}

Nova quantidade de maçã:  5

{'maçã': 5, 'banana': 6, 'vitaminas': {'a': 'boa para pele'}, 'laranja': 10}

{'cachorro': 'Batolomeu'}

{'nome': 'Victor', 'idade': 24, 'hobbies': ['jogar xadrez', 'esportes']}

"""