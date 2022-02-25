"""Dicionário

Escreva uma função que simula a função dict() do Python.
"""

def myDict(**keywords: dict) -> dict:
    return keywords

print(myDict(a=10, b=20, c=30, d=40, e=50))
