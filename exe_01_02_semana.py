"""Dias da semana

Faça um programa que leia um número e exiba o dia correspondente da
semana. (1-Domingo, 2- Segunda, etc.). Se digitado outro valor deve
aparecer uma menagem de erro
"""

while True:
    day = int(input('Introduza o dia: '))
    if (day > 0) and (day < 8):
        break
    print('Opção inválida! Deve escolher entre 1 e 7.')

if day == 1:
    print('Domingo')
elif day == 2:
    print('Segunda-feira')
elif day == 3:
    print('Terça-feira')
elif day == 4:
    print('Quarta-feira')
elif day == 5:
    print('Quinta-feira')
elif day == 6:
    print('Sexta-feira')
else:
    print('Sabado')

# match day:
#     case 1:
#         print('Domingo')
#     case 2:
#         print('Segunda-feira')
#     case 3:
#         print('Terça-feira')
#     case 4:
#         print('Quarta-feira')
#     case 5:
#         print('Quinta-feira')
#     case 6:
#         print('Sexta-feira')
#     case 7:
#         print('Sabado')
