"""
Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. 
Elas querem um programa que mostre:

Quais itens apareceram nas duas listas
Quais foram exclusivos de Laura
Quais foram exclusivos da Ana

lista_comida_ana = [pão, leite, ovos, carne]
lista_comida_leticia = [leite, açucar, mel, frango, morangos, cheiro verde,]
"""

lista_ana  = ["pão", "leite", "ovos", "carne"]
lista_leticia = ["leite", "açucar", "mel", "ovos", "frango", "morangos", "cheiro verde", "frango"]

comidas_emcomum = set(lista_ana).intersection(set(lista_leticia))
print(comidas_emcomum)
comidas_diferentes_ana = set(set(lista_ana) - set(lista_leticia))
print(comidas_diferentes_ana)
comidas_diferentes_leticia = set(set(lista_leticia) - set(lista_ana))
print(comidas_diferentes_leticia)

