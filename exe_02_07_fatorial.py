"""Fatorial

Faça um programa que calcule o fatorial de um número inteiro fornecido
pelo utilizador. A saída deve ser formatada, como no exemplo. Deve ser
utilizado o clico for.

Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

n = int(input('Introduza o valor de N: '))
f = 1

print(f'{n}! =', end=' ')
for i in reversed(range(1, n + 1)):
    print(i, end=' ')
    f *= i
    if i != 1:
        print('x', end=' ')
print(f'= {f:,}')
