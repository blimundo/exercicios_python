"""Comissão

Uma empresa paga seus vendedores com base em comissões. O vendedor
recebe 5.000$00 por semana mais 9% de suas vendas brutas daquela
semana. Por exemplo, um vendedor que teve vendas brutas de 30.000$00 em
uma semana recebe 5.000$00 mais 9% de 30.000$00, ou seja, um total de
7.700$00. Escreva um programa que determine quantos vendedores
receberam salários nos seguintes intervalos de valores:
    *  5.000 -  5.999
    *  6.000 -  6.999
    *  7.000 -  7.999
    *  8.000 -  8.999
    *  9.000 - 9.999
    * 10.000 - 10.999
    * 11.000 - 11.999
    * 13.000 em diante

Desafio: crie uma fórmula para chegar na posição da lista a partir do 
salário, sem fazer vários ifs aninhados.
"""

salaryMap = [
    {'min': 5000, 'max': 5999},
    {'min': 6000, 'max': 6999},
    {'min': 7000, 'max': 7999},
    {'min': 8000, 'max': 8999},
    {'min': 9000, 'max': 9999},
    {'min': 10000, 'max': 10999},
    {'min': 11000, 'max': 11999},
    {'min': 13000, 'max': 999999},
]
salaries = []

while True:
    salary = int(input('Introduza o valor de vendas (-1 para a leitura): '))
    if salary == -1:
        break
    elif salary < 0:
        print('O valor não pode ser negativo! Leitura ignorada.')
        continue
    salaries.append(5000 + salary * 0.09)

print()
for row in salaryMap:
    count = sum(map(lambda salary: (salary >= row['min']) and (salary < row['max']), salaries))
    band = f"[{row['min']}$00-{row['max']}$00]"
    print(f'{band:^20}: {count}')
