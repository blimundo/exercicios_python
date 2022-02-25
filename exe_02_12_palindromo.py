"""Palíndromo

Palíndromo é uma palavra, frase ou número que permanece igual quando
lida de trás para diante. Escreva um programa que lê uma string e
determina se a mesma é um palíndromo. 
"""

word = input('Introduza a palavra: ').lower()
length = len(word)
flag = True
i = 0

while i < length:
    if word[i] != word[-i - 1]:
        flag = False
        break
    i += 1

if flag:
    print(f"\n'{word}' é palíndromo")
else:
    print(f"\n'{word}' não é palíndromo")
