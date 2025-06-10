"""
Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade 
de um item específico no estoque. Sua tarefa é criar um programa que solicite o nome do 
produto e a nova quantidade, atualizando essa informação no dicionário de estoque.

input:

estoque = { 

    "Caderno universitário": 50, 

    "Caneta azul": 120, 

    "Borracha branca": 30 

} 

Nome do produto a ser atualizado: Caneta azul 

Nova quantidade: 150 

output:

{ 

    "Caderno universitário": 50, 

    "Caneta azul": 150, 

    "Borracha branca": 30 

} 
"""

estoque = { 
"caderno universitário": 50, 
"caneta azul": 120, 
"borracha branca": 30} 

produto_atualizar = input("Digite o nome do produto que deseja atualizar: ").lower()
if produto_atualizar in estoque.keys():
    valor = int(input("Digite a quantidade: "))
    estoque[produto_atualizar] = valor
    print("produto atualizado!")
else:
    print("o produto não existe!")
print(estoque)
