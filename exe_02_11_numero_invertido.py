"""Número invertido

Faça um programa que peça um numero inteiro positivo e em seguida
mostre este numero invertido.
Exemplo: 123456789 deverá ter como saída 987654321.
"""

number = input('Introduza o número: ')
reversedNumber = []

for i in reversed(number):
    reversedNumber.append(i)

# Sem o uso de for
# reversedNumber = list(reversed(number))

print(''.join(reversedNumber))
