"""Conjuntos

Faça um programa que leia duas listas com 10 elementos cada. Gere e
exiba (por ordem crescente):
    - Uma lista com elementos que conste em ambas as listas
      (interseção);
    - Uma lista com elementos das duas listas, sem repetir (união);
    - Uma lista com os 20 elementos, cujos valores deverão ser
      compostos pelos elementos intercalados das duas listas.
"""

set_1 = numbers = list(map(int, input('Introduza 10 números: ').split()))
set_2 = numbers = list(map(int, input('Introduza 10 números: ').split()))

intersection = [ i for i in set_1 if i in set_2 ]

union = set_1.copy()
union.extend([ i for i in set_2 if i not in union ])

combined = []
size = max(len(set_1) , len(set_2))
for i in range(size):
    try:
        combined.append(set_1[i])
    except IndexError:
        pass

    try:
        combined.append(set_2[i])
    except IndexError:
        pass

intersection.sort()
union.sort()

print(f'Intersecção: {intersection}')
print(f'União: {union}')
print(f'Combinado: {combined}')
