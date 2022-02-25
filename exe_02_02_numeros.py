"""Números

Faça um programa que imprima na tela os números de 1 a 20, um abaixo do
outro. Depois modifique o programa para que ele mostre os números um ao
lado do outro. Deve ser utilizado o ciclo do-while.
"""

i = 0
while True:
    if i > 20:
        break
    print(i, end=' ')
    i += 1
print()