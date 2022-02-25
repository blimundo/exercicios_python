"""Dicionário

Escreva uma list comprehension que crie um dicionário em que cada chave
corresponde a um outro dicionário, contendo nome e a nota do aluno.

NOTA: O nome e a nota podem ter valor None.
"""

d = { 'student_' + str(i): {'name': None, 'score': None} for i in range(3) }

print(d)
