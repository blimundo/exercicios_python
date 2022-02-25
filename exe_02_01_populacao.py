"""População

Supondo que a população de um país A seja da ordem de 80.000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja 
200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
que calcule e escreva o número de anos necessários para que a população
do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.
"""

countryA = {'pop': 80000, 'tax': 0.03}
countryB = {'pop': 200000, 'tax': 0.015}

year = 0
while countryB['pop'] > countryA['pop']:
    countryA['pop'] += countryA['pop'] * countryA['tax']
    countryB['pop'] += countryB['pop'] * countryB['tax']
    year += 1

print(f'São necessários {year} anos para que a população de A ultrapasse a população de B.')