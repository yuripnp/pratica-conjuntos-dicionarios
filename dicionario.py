# formas de criar dicionarios
dicionarioUm = {'a': 1, 'b': 2, 'c': 3}
dicionarioDois = dict(a=1, b=2, c=3)
dicionarioVazio = {}
lista_de_tuplas = [('a', 1), ('b', 2), ('c', 3)]
dicionarioTres = dict(lista_de_tuplas)

# adicionar elementos ao dicionario
dicionarioUm['d'] = 4
print(dicionarioUm)

print(dicionarioUm['a'])
print(dicionarioUm.get('a'))
print(dicionarioUm.get('d'))
print(dicionarioUm.get('d', 'Não encontrado'))

print(dicionarioUm.keys())
print(dicionarioUm.values())
print(dicionarioUm.items())

# remover elementos do dicionario
print(dicionarioUm.pop('a'))

print(len(dicionarioUm.keys()))
print('a' in dicionarioUm.keys())
print('a' in dicionarioUm.values())

# copiar dicionario
dicionarioCopia = dicionarioUm.copy()
print(dicionarioCopia)

estoque = {
    "frutas":set(["maçã", "uva", "laranja"]),
    "legumes":set(["batata", "cenoura", "tomate"]),
    "bebidas":set(["água", "refrigerante", "suco"])
}

# atualizar dicionario
estoque["frutas"].add("banana")
print(estoque)

estoque["frutas"].remove("banana")
print(estoque)

# adicionar elementos ao dicionario
estoque["frutas"].add("banana")
print(estoque)

# remover elementos do dicionario
estoque["frutas"].remove("banana")
print(estoque)