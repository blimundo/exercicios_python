"""Primo

Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo. Um número primo é aquele que é divisível somente por ele
mesmo e por 1.
"""

number = int(input('Introduza o número: '))
count = 0
i = 1

while i <= number:
    if number % i == 0:
        count += 1
    i += 1

if count < 3:
    print(f'{number} é um número primo.')
else:
    print(f'{number} não é um número primo.')
