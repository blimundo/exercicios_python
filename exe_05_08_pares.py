"""Pares

Escreva uma função que receba uma lista de inteiros e utilize a função
filter() para retornar uma nova lista contendo apenas os números pares.
"""

def onlyEvens(numbers: list) -> list:
    evens = filter(lambda x: not x % 2, numbers)
    return list(evens)

if __name__ == '__main__':
    numbers = map(int, input('Introduza os números: ').split())
    print(f'\nPares: {onlyEvens(numbers)}')
