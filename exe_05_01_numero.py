"""Números

Faça um programa que produza o resultado abaixo (sendo N fornecido pelo
utilizador). O exercício deve ser resolvido utilizando recursão.

1
1 2
1 2 3
...
1 2 3 ... N
"""

def show(n: int) -> None:
    if n > 0:
        show(n - 1)
    i = 1
    while i < n + 1:
        print(f'{i:>3} ', end='')
        i += 1
    print()

if __name__ == '__main__':
    n = int(input('Introduza o valor de N: '))
    show(n)
