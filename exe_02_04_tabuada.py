"""Tabuada
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O utilizador deve informar de qual numero
ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
    Tabuada de 5:
        5 x 1 = 5
        5 x 2 = 10
        ...
        5 x 10 = 50
"""

n = int(input('Introduza o número: '))
while (n < 1) and (n > 9):
    n = int(input('Introduza um número entre 1 e 9: '))

print(f'\nTabuada de {n}:')
for i in range(1, 11):
    print(f'\t{i:>2} x {n} = {i * n:>2}')
    