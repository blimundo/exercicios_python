"""Frutas

Uma fruteira está vendendo frutas com a seguinte tabela de preços:
Fruta       < 5KG       >= 5KG
Morango     250$00      220$00
Maçã        180$00      150$00  

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar 2.500$00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a 
quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago 
pelo cliente.
"""

strawberries = float(input('Introduza a quantidade de morangos (em KG): '))
apples = float(input('Introduza a quantidade de maçãs (em KG): '))

priceStrawberries = 250 if strawberries < 5 else 220
priceApples = 180 if apples < 5 else 150

total = (strawberries * priceStrawberries) + (priceApples * apples)

if (strawberries + apples) > 8:
    total *= 0.9

print(f'\nTotal a pagar: {total:,.0f}$00')