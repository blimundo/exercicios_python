"""Lista

Escreva uma função que simula a função list() do Python.
"""

def myList(*arguments: tuple) -> list:
    return list(arguments)

print(myList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
