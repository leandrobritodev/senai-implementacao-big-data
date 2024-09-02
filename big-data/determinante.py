### Matrizes - Exercício 2  ###

import random as rd
print("=" * 5 + "Determinante de Matrizes" + "=" * 5)
matriz1 = [[rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)], [rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)], [rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)]]

print("Matriz:", [matriz1[0][1], matriz1[1][0], matriz1[2][2] + matriz1[0][0], matriz1[1][2], matriz1[2][1], matriz1[0][2], matriz1[1][1], matriz1[2][0]])
determinante = [(matriz1[0][0] * matriz1[1][1] * matriz1[2][2] + matriz1[0][1] * matriz1[1][2] * matriz1[2][0] + matriz1[0][2] * matriz1[1][0] * matriz1[2][1]) - (matriz1[0][1] * matriz1[1][0] * matriz1[2][2] + matriz1[0][0] * matriz1[1][2] * matriz1[2][1] + matriz1[0][2] * matriz1[1][1] * matriz1[2][0])]

print("Determinante:", sum(determinante))
