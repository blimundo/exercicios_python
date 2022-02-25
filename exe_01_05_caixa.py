"""Caixa eletrônico

Faça um Programa para um caixa eletrônico. O programa deverá perguntar
ao utilizador o valor a ser levantado e depois informar quantas notas
de cada valor serão fornecidas. As notas disponíveis são de 200, 500,
1.000, 2.000, 5.000 escudos. O valor mínimo é de 200 escudos e o máximo
de 20.000 escudos. O programa não deve se preocupar com a quantidade de
notas existentes na máquina.

Exemplo: para retirar 16.700 escudo, a máquina deverá fornecer:
    - 3 notas de 5.000
    - 1 nota de 1.000
    - 1 nota de 500
    - 1 nota de 200
"""

amount = int(input('Introduza o valor a ser levantado: '))

if (amount < 200) or (amount > 20000): 
    print('Valor inválido!')
    exit(-1)

print('Notas:')
total = 0
for i in [5000, 2000, 1000, 500, 200]:
    n = int(amount / i)
    if n > 0:
        print(f'{"":3} * {n:>2} x {i:>5,}$00')
    total += i * n
    amount = amount - (i * n)
    if amount < 0:
        break

print(f'Total levantado: {total:,.0f}$00')
