### Matrizes - Exercício 1  ###

import random as rd
print("=" * 5 + "Matrizes" + "=" * 5)
matriz1 = [[rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)], [rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)], [rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)]]
matriz2 = [[rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)], [rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)], [rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)]]

print("Matriz 1: ", matriz1)
print("Matriz 2: ", matriz2)
soma1 = [matriz1[1][0] + matriz1[2][0] + matriz1[2][1]]
soma2 = [matriz2[0][1] + matriz2[0][2] + matriz2[1][2]]
resultado = sum(soma1) + sum(soma2)

print("Matriz 1: ", [matriz1[1][0], matriz1[2][0], matriz1[2][1]])
print("Matriz 2: ", [matriz2[0][1], matriz2[0][2], matriz2[1][2]])
print("Soma da matriz 1: ", soma1)
print("Soma da matriz 2: ", soma2)
print("Soma da matrizes: ", resultado)


