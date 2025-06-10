"""
Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria.
Ela precisa de um programa que permita cadastrar produtos em forma de dados estruturados.
O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, 
exibir as informações cadastradas em um dicionário, onde cada produto será uma 
chave e a quantidade correspondente será o valor.

input:
Digite o nome do produto: Caneta
Digite a quantidade: 30

output:
Dicionário de produtos: {'Caneta': 50, 'Caderno': 30, 'Borracha': 20} 
"""

produtos = {}
operador = "s"
while operador != "n":
    produto = input("Digite o nome do produto: ").lower()
    if produto in produtos.keys():
        print("O produto já foi cadastrado, insira outro.")
        continue
    quantidade = int(input("Digite a quantidade: "))
    produtos[produto] = quantidade
    operador = input("Deseja inserir mais algum produto (s/n): ")

print(produtos)

 