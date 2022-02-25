"""Primo 2

Faça um programa que mostre todos os primos entre 1 e N sendo N um
número inteiro fornecido pelo utilizador. O programa deverá mostrar
também o número de divisões que ele executou para encontrar os números
primos.
"""

def isPrime(number: int) -> bool:
    count = 0
    i = 1
    while i <= number:
        if number % i == 0:
            count += 1
        i += 1
    if count < 3:
        return True
    return False

number = int(input('Introduza o número: '))
primes = []
divisons = 0

for i in range(1, number + 1):
    if isPrime(i):
        primes.append(i)
    divisons += i

print(f'\nNúmeros primos menores do que {number}: {primes}')
print(f'Foram executados {divisons} operações de divisão.')
