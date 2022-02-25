"""Alunos

Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que
lê os registos de um ficheiro e determine quantos alunos com mais de 13
anos possuem altura inferior à média de altura desses alunos.
"""

students = []

# read all records from file
with open('alunos.txt', 'r') as file:
    for line in file.readlines():
        age, height = line.split()
        students.append({
            'age': int(age), 
            'height': float(height)
        })

# calculate average height
sum = 0
for student in students:
    sum += student['height']
average = sum / len(students)

# count students 
tallestsStudents = filter(lambda student: student['height'] > average and student['age'] > 13, students)
del students

print(f'A média de altura dos alunos é de {average:.2f}.')
print(f'O total de alunos maiores de 13 anos e cuja altura é superior a média é de {len(list(tallestsStudents))}.')
