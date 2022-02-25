"""List comprehension

a) Lista com valores 0
    Crie uma lista de 25 elementos, todos iguais a zero.

b) Pares
    Crie uma lista com números pares, menores do que 100.

c) Lista multidimensional
    Crie uma matriz 5x5, inicializado com o valor 0.
"""

# a)
zeros = [ 0 for i in range(25) ]
print('\nZeros:')
print(zeros)

# b)
even = [ i for i in range(100) if i % 2 == 0 ]
# even = [ i for i in range(0, 100, 2) ]    # Outra forma de obter a mesma lista
print('\nPares:')
print(even)

# c)
matrix = [ [j for j in range(5)] for i in range(5) ]
print('\nMatriz:')
for row in matrix:
    print(row)
