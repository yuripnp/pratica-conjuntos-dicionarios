# formas de criar conjuntos
conjuntoUm = {1, 2, 3, 4, 5}
conjuntoDois = set([1, 2, 3, 4, 5])
conjunto_vazio = set()

print(3 in conjuntoUm) # True
print(3 not in conjuntoUm) # False

# adicionar elementos ao conjunto
conjuntoUm.add(6)
conjuntoDois.update([6, 7, 8])
print(conjuntoUm) # {1, 2, 3, 4, 5, 6}

# remover elementos do conjunto
conjuntoUm.remove(6)
print(conjuntoUm) # {1, 2, 3, 4, 5}
# adicionar elementos ao conjunto
conjuntoUm.add(6)
print(conjuntoUm)

# remover elementos do conjunto
conjuntoUm.remove(6)
print(conjuntoUm)

# metodos de operacoes com conjuntos
conjuntoUm = {1, 2, 3, 4, 5}
conjuntoDois = {6, 7, 8, 9, 10}

# uniao de conjuntos
uniao = conjuntoUm | conjuntoDois
print(uniao) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# intersecao de conjuntos
intersecao = conjuntoUm & conjuntoDois
print(intersecao) # {1, 2, 3, 4, 5}

# diferenca de conjuntos
diferenca = conjuntoUm - conjuntoDois
print(diferenca) # {1, 2, 3, 4, 5}

# diferenca simetrica de conjuntos
diferenca_simetrica = conjuntoUm ^ conjuntoDois
print(diferenca_simetrica) # {6, 7, 8, 9, 10}

# verificando se um conjunto é subconjunto de outro
subconjunto = conjuntoUm.issubset(conjuntoDois)
print(subconjunto) # False

# verificando se um conjunto é superconjunto de outro
superconjunto = conjuntoUm.issuperset(conjuntoDois)
print(superconjunto) # False

# verificando se um conjunto é disjunto de outro
disjunto = conjuntoUm.isdisjoint(conjuntoDois)
print(disjunto) # True

# verificando se um conjunto é igual a outro
igual = conjuntoUm == conjuntoDois
print(igual) # False

# verificando se um conjunto é diferente de outro
diferente = conjuntoUm != conjuntoDois
print(diferente) # True

print(len(conjuntoUm)) # 5
print(max(conjuntoUm)) # 5
print(min(conjuntoUm)) # 1
print(sum(conjuntoUm)) # 15

conjuntoCopia = conjuntoUm.copy()