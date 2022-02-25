"""Alunos

Escreva um programa que lê duas notas de vários alunos e armazena tais
notas em um dicionário, onde a chave é o nome do aluno. A entrada de
dados deve terminar quando for lida uma string vazia como nome.
De seguida o programa deverá perguntar um nome ao utilizador e imprimir
as notas e a média do aluno.
"""

students = {}

while True:
    name = input('Introduza o nome (string vazia para a leitura): ').lower()
    if not name:
        break
    students[name] = {
        'score_1': float(input(f'Introduza a primeira nota do aluno {name}: ')),
        'score_2': float(input(f'Introduza a segunda nota do aluno {name}: ')),
    }
    print()

while True:
    print('\n')
    name = input('Introduza o nome de um aluno (string vazia termina o programa): ').lower()
    if not name:
        break
    student = students.get(name)
    if student is None:
        print(f'O aluno {name} não existe!')
        continue
    average = (student['score_1'] + student['score_2']) / 2
    print(f'\nNotas do aluno {name}:')
    print(f"\tNota 1: {student['score_1']:.1f}")
    print(f"\tNota 2: {student['score_2']:.1f}")
    print(f"\t Média: {average:.1f}")
