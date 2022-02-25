"""Consoantes

Faça um programa que leia um vetor de 10 caracteres, e diga quantas
consoantes foram lidas. Imprima as consoantes.
"""

consonants = 'bcdfghjklmnpqrstvxyz'
word = input('Introduza a palavra: ').lower()
totals = { i: word.count(i) for i in consonants if word.count(i) }

print('-' * 10)
for consonant in totals.keys():
    print(f'| {consonant.upper()} | {totals[consonant]:>2} |')
    print('-' * 10)
