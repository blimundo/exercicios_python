"""Triangulo

Faça um programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados 
formem um triângulo, se o mesmo é equilátero, isósceles ou escaleno.

Dicas:
    - Três lados formam um triângulo quando a soma de quaisquer dois
      lados for maior que o terceiro;
    - Triângulo Equilátero: três lados iguais;
    - Triângulo Isósceles: quaisquer dois lados iguais;
    - Triângulo Escaleno: três lados diferentes;
"""

a, b, c = map(int, input('Introduza os 3 valores: ').split())

if (a+b > c) or (a+c > b) or (c+b) > a:
    if (a == b) and (b == c):
        print('É um triangulo equilátero.')
    elif (a == b) or (a == c):
        print('É um triangulo isósceles.')
    else:
        print('É um triangulo escaleno.')
else:
    print('Não é um triangulo.')
