"""Soma

Escreva uma função que receba um número variável de valores numéricos e
retorne a soma desses números.
"""

def mySum(*arguments: tuple) -> float:
    sum = 0
    for i in arguments:
        sum += i
    return sum

sum = mySum(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f'1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = {sum}')
