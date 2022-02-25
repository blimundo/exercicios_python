"""Números

Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando for
informado um valor igual a -1 (que não deve ser armazenado). Após esta
entrada de dados, faça:
    - Mostre a quantidade de valores que foram lidos;
    - Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    - Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    - Calcule e mostre a soma dos valores;
    - Calcule e mostre a média dos valores;
    - Calcule e mostre a quantidade de valores acima da média calculada;
    - Calcule e mostre a quantidade de valores abaixo de sete;
    - Encerre o programa com uma mensagem.
"""

scores = []

# Leitura dos valores
while True:
    score = int(input('Introduza a nota (-1 para a leitura): '))
    if (score < -1) or (score > 10):
        print('Nota inválida! Leitura ignorada.')
        continue
    elif score == -1:
        break
    scores.append(score)

# Exibe o total de registos lidos
totalScore = len(scores)
print(f'\nTotal de registos lidos: {totalScore}')

# Exibe os registos lidos (em ordem de leitura)
print(f'Valores lidos: ', end='')
flag = False
for score in scores:
    if flag:
        print(f', {score}', end='')
    else:
        print(f'{score}', end='')
        flag = True
print()

# Exibe os registos lidos (em ordem inversa da leitura)
print(f'Valores lidos (em ordem reversa): ')
for score in reversed(scores):
    print(score)

# Exibe a soma dos valores
sum = sum(scores)
print(f'Soma dos valores: {sum}')

# Exibe a média dos valores
average = sum / totalScore
print(f'Média dos valores: {average:.2f}')

# Exibe a quantidade de valores superiores a média e a quantidade de valores
# inferiores a 7
totalAverage = 0
totalSeven = 0
for score in scores:
    if score >= average:
        totalAverage += 1
    if score < 7:
        totalSeven += 1
print(f'Total de notas superiores a média: {totalAverage}')
print(f'Total de notas inferiores a 7: {totalSeven}')

# Exibe a mensagem final
print('Adeus...')
