"""
Ana está organizando uma festa de aniversário e precisa de uma lista de convidados 
que não tenha repetições , pois algumas pessoas foram convidadas mais de uma vez por engano. 
Ela gostaria que o programa solicitasse o nome dos convidados e, ao final, exibisse a 
lista organizada sem repetições.

input:
nome do convidado: Ana
nome do convidado: Luiza
nome do convidado: Pedro

output:
lista de convidados: Ana, Luiza, Pedro
"""

convidados = []
comando = "s"

while comando == "s":
    nome = input("nome do convidado: ")
    if nome not in convidados:
        convidados.append(nome)
    else:
        print("esse convidado já está na lista")
    comando = input("deseja entrar mais algum convidado? (s/n): ")

print(f"lista de convidados: {convidados}")