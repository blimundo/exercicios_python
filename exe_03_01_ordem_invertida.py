"""Ordem inversa

Faça um Programa que leia um vetor de 10 números reais e mostre-os na
ordem inversa.
"""

numbers = list(map(int, input('Introduza 10 números: ').split()))

inverse = [numbers[i] for i in range(0, len(numbers), -1)]

print(f'Ordem inversa: {inverse}')
