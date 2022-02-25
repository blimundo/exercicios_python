"""Pares e impares

Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números impares. O 
programa deve usar o ciclo while.
"""

nums = list(map(int, input('Introduza 10 números: ').split()))

odd = 0
even = 0

for i in nums:
    if i % 2:
        odd += 1
    else:
        even += 1

print(f'\nA lista tem {even} pares e {odd} impares.')
