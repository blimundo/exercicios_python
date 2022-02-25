"""Quadrado mágico

Um quadrado mágico é aquele dividido em linhas e colunas, com um número
em cada posição e no qual a soma das linhas, colunas e diagonais é a
mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de
1 a 9:
    8  3  4
    1  5  9
    6  7  2
Elabore um programa que identifica e mostra na tela todos os quadrados
mágicos com as características acima. 

Dica: produza todas as combinações possíveis e verifique a soma quando
completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples
que usar uma matriz 3x3.
"""

from itertools import permutations

def isMagicSquare(table: list) -> bool:
    if (table[0] + table[1] + table[2]) != (table[3] + table[4] + table[5]) != (table[6] + table[7] + table[8]):
        return False
    if (table[0] + table[3] + table[6]) != (table[1] + table[4] + table[7]) != (table[2] + table[5] + table[8]):
        return False
    if (table[0] + table[4] + table[8]) != (table[2] + table[4] + table[6]):
        return False
    return True

def printTable(table: list) -> None:
    i = 0
    while i < len(table):
        if (i % 3 == 0) and (i != 0):
            print()
        print(f' {i} ', end='')
        i += 1
    print('\n', '-' * 8)

if __name__ == '__main__':
    count = 0
    for table in permutations([i for i in range(1, 10)]):
        if isMagicSquare(table):
            printTable(table)
            count += 1
    print(f'\nForam encontrados {count:,} quadrados mágicos.')
