""""Fibonacci

Na matemática, a sequência de Fibonacci, é uma sequência de números
inteiros, começando normalmente por 0 e 1, na qual cada termo
subsequente corresponde à soma dos dois anteriores (exemplo: 1,1,2,3,5,
8,13,21,34,55...). Faça um programa que pede um inteiro N e escreva os
N primeiros elementos da sequência Fibonacci.
"""

n = int(input('Introduza o valor de N: '))

a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

print()
