"""
Clara é editora de uma revista e deseja comparar dois artigos 
para identificar quais palavras aparecem em ambos. Sua tarefa é criar um 
programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.

input:
texto 1: O dia está muito lindo
texto 2: O Sol está muito brilhante

output:
palavras em comum: ["O", "está", "muito"]
"""

texto_um = "O dia está muito lindo"
texto_dois = "O Sol está muito brilhante"

conjunto_um = set(texto_um.split())
conjunto_dois =  set(texto_dois.split())

conjunto_intersection = conjunto_um.intersection(conjunto_dois)
print(f"As palavras iguais são {conjunto_intersection}")
