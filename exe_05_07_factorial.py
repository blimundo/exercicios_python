"""Fatorial

Escreva uma função recursiva que calcule o fatorial de um inteiro N.
"""

def fatorial(n: int) -> int:
    if n < 0:
        raise ValueError('N não pode ser negativo')
    elif n == 1:
        return 1
    return n * fatorial(n - 1)

if __name__ == '__main__':
    n = int(input('Introduza o valor de N: '))
    f = fatorial(n)
    print(f'Factorial de {n} é {f}')
