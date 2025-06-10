"""
Laura está organizando um workshop sobre tecnologia e precisa de um programa 
que permita remover participantes que desistiram do evento. O sistema armazena os 
participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto 
com os dados do participante. O programa deve solicitar o nome de um participante e 
remover esse nome da lista de participantes registrados, caso exista.

input:

participantes = { 
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 
} 


Nome do participante a ser removido: Carla 

output:

Lista atualizada de participantes: 

Workshop 1: {'Alice', 'Bruno', 'Diego'} 
Workshop 2: {'Fernanda', 'Gustavo', 'Helena'} 
"""
participantes = { 
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 
} 

nome = input("Nome do participante a ser removido: ")

removido = False
for workshop, nomes in participantes.items():
    if nome in nomes:
        nomes.remove(nome)
        print(f"{nome} removido de {workshop}")
        removido = True

if not removido:
    print(f"{nome} não encontrado em nenhum workshop.")

print("\nLista atualizada de participantes:")
for workshop, nomes in participantes.items():
    print(f"{workshop}: {', '.join(nomes)}")