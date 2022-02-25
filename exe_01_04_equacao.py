"""Equação segundo grau

Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c 
e fazer as consistências, informando ao usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero, a equação não é
      do segundo grau e o programa não deve fazer pedir os demais
      valores, sendo encerrado;
    - Se o delta calculado for negativo, a equação não possui raízes
      reais. Informe ao usuário e encerre o programa;
    - Se o delta calculado for igual a zero a equação possui apenas uma
      raiz real; informe-a ao usuário;
    - Se o delta for positivo, a equação possui duas raízes reais;
      informe-as ao usuário.
"""

from math import sqrt


a, b, c = map(int, input('Introduza os valores de a, b e c: ').split())

if a == 0:
    print(f'{a}x2 + {b}x + {c} não é um equação do segundo grau!')
    exit(-1)

delta = b**2 - 4 * a * c

if delta < 0:
    print(f"'{a}x2 + {b}x + {c}' não possui raízes reais!")
elif delta == 0:
    x = (-b + sqrt(delta)) / (2 * a)
    print(f"'{a}x2 + {b}x + {c}' possui uma raiz que é x={x:.2f}.")
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f"'{a}x2 + {b}x + {c}' possui duas raízes que são é x1={x1:.2f} e x2={x2:.2f}.")
