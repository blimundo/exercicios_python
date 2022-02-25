"""Conversão para dicionário

Escreva um programa que converta a lista abaixo num dicionário.
l = [
    ['carlos', 15, 12],
    ['alberto', 9, 15],
    ['maria', 18, 19]
]

Formato nome: nota1, nota2
"""

l = [
    ['carlos', 15, 12],
    ['alberto', 9, 15],
    ['maria', 18, 19]
]
d = {}

for row in l:
    d[row[0]] = [row[1], row[2]]

print(d)
