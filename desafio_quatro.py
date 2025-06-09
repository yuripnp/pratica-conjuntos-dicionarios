"""
Marina trabalha no setor de segurança de uma empresa e precisa verificar se um 
determinado conjunto de permissões faz parte das permissões principais de um sistema. 
Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique 
se a segunda lista está contida na primeira.

input:

> CASO 01: 
Permissões principais: leitura, escrita, execução, compartilhamento 
Permissões solicitadas: leitura, escrita 

> CASO 02: 
Permissões principais: leitura, escrita, execução, compartilhamento 
Permissões solicitadas: leitura, exclusão 

output:

> CASO 01: 
As permissões solicitadas fazem parte das permissões principais. 
> CASO 02: 
As permissões solicitadas não fazem parte das permissões principais. 
"""
def verificar_permissoes(conjunto_principal, subconjunto):
    if subconjunto.issubset(conjunto_principal):
        print(f"As permissões solicitadas fazem parte das permissões principais. ")
    else:
        print(f"As permissões solicitadas não fazem parte das permissões principais.")


permissoes_principais = {"leitura", "escrita", "execução", "compartilhamento"}
permissao_usuario_um = {"leitura", "escrita"}
permissao_usuario_dois = {"leitura","exclusão"}

verificar_permissoes(permissoes_principais, permissao_usuario_um)
verificar_permissoes(permissoes_principais, permissao_usuario_dois)

    

