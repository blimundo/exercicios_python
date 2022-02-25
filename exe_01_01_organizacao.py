"""Organizações Tabajara

As Organizações Tabajara irão atribuir um aumento de salário aos seus colaboradores e lhe
contrataram para desenvolver o programa que irá calcular os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
critério, baseado no salário atual:
    - salários até 18.000$00 (incluído): aumento de 20%
    - salários entre 18.000$00 e 27.000$00 (incluído): aumento de 15%
    - salários entre 27.000$00e 45.000$00 (incluído): aumento de 10%
    - salários de 45.000$00 em diante: aumento de 5%

Após o aumento ser realizado, informe na tela:
    - salário antes do reajuste;
    - percentual de aumento aplicado;
    - valor do aumento;
    - novo salário, após o aumento.
"""
salary = int(input('Introduza o salário: '))
perc = 0

if salary > 45000:
    perc = 5
elif salary > 27000:
    perc = 10
elif salary > 18000:
    perc = 15
else:
    perc = 20

new_salary = salary * (1 + perc / 100)
dif = new_salary - salary

print('-' * 46)
print('| {:^10s} | {:^3s} | {:^10s} | {:^10s} |'.format('Sal. Atual', '%', 'Aumento', 'Novo Sal.'))
print('-' * 46)
print('| {:>7,.0f}$00 | {:>2}% | {:>7,.0f}$00 | {:>7,.0f}$00 |'.format(salary, perc, dif, new_salary))
print('-' * 46)
