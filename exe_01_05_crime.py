"""Crime

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    - "Telefonou para a vítima?"
    - "Esteve no local do crime?"
    - "Mora perto da vítima?"
    - "Devia para a vítima?"
    - "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime. Se a pessoa responder positivamente a 2 questões
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como 
"Inocente".
"""

def getAnswer(question: str) -> bool:
    while True:
        answer = input(question + ' ').lower()
        if answer in ['s', 'sim', 'n', 'nao', 'não']:
            break
        print("Digite 's' ou 'sim' para resposta afirmativa; 'n', 'nao' ou 'não' para resposta negativa.")
    if answer in ['s', 'sim']:
        return True
    return False

questions = [
    'Telefonou para a vítima?',
    'Esteve no local do crime?',
    'Mora perto da vítima?',
    'Devia para a vítima?',
    'Já trabalhou com a vítima?',
]
answers = []

for question in questions:
    answers.append(getAnswer(question))

totalYes = answers.count(True)

if totalYes == 2:
    print('\nA pessoa é suspeita.')
elif totalYes == 5:
    print('\nA pessoa é o assasino')
elif totalYes < 2:
    print('\nA pessoa é inocente.')
else:
    print('\nA pessoa é cúmplice.')
