"""Números 2

Faça um programa que leia 5 números e informe:
    - o maior número;
    - o menor número;
    - a soma dos números;
    - a média dos números.
"""

nums = list(map(int, input('Introduza 5 números: ').split()))

maior = -9999
menor = 9999
soma = 0
for n in nums:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
media = soma / 5

# Sem uso de loop:
# maior = max(nums)
# menor = min(nums)
# soma = sum(nums)
# media = soma / len(nums)

print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Soma: {soma}')
print(f'Média: {media:.2f}')



