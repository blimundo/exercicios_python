"""Quadrado

Escreva uma função que receba uma lista de inteiros e utilize a função
map() para retornar uma nova lista contendo o quadrado de cada número.
"""

def square(numbers: list) -> list:
    squares = map(lambda x: x**2, numbers)
    return list(squares)

if __name__ == '__main__':
    numbers = map(int, input('Introduza os números: ').split())
    print(f'\nQuadrados: {square(numbers)}')
