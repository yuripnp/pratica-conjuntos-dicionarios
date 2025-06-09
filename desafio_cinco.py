"""
Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas 
equipes distintas. Após unir as listas, ela quer remover uma tarefa específica 
informada pelo usuário. Sua tarefa é criar um programa que realize essa operação.

input:
equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 

output:

Tarefas finais: {'implementar funcionalidade', 'planejar reunião', 'revisar documento', 'corrigir bug'} 
"""
equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 

tarefas_finais = equipe_a | equipe_b
print(tarefas_finais)

tarefa_remover = input("Tarefa a ser removida: ").lower()

if tarefa_remover in tarefas_finais:
    tarefas_finais.remove(tarefa_remover)
print(f"{tarefas_finais}")