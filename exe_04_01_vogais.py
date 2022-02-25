"""Vogais

Escreva um programa que pede uma string ao utilizador e conta todas as 
vogais presentes na string recebido, escrevendo na tela um dicionário
contendo a quantidade de cada vogal. 
"""

text = input('Introduza o texto a ser analisado: ').lower()
vogals = list('aeiou')
count = dict.fromkeys(vogals, 0)

for char in text:
    if char in vogals:
        count[char] += 1

print('-' * 10)
for vogal in vogals:
    print(f'| {vogal.upper()} | {count[vogal]:>2} |')
    print('-' * 10)
