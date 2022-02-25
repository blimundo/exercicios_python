"""Metereologia

O Departamento de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas, e
informe ao final a menor e a maior temperatura informadas, bem como a 
média das temperaturas. As temperaturas devem ser lidas de um ficheiro. 
"""

larger = -1
smaller = 9999
tempCount = 0
tempSum = 0

with open('G:\exercicios_python\\temperaturas.txt', 'r') as file:
    for line in file.readlines():
        temperature = float(line)
        if temperature > larger:
            larger = temperature
        elif temperature < smaller:
            smaller = temperature
        tempCount += 1
        tempSum += temperature

print(f'Maior temperatura: {larger:.2f}')
print(f'Menor temperatura: {smaller:.2f}')
print(f'Média das temperaturas: {tempSum / tempCount:.2f}')
