### Matrizes - Exercício 3  ###

import numpy as np
import random as rd
print("=" * 5 + "Determinante de Matrizes" + "=" * 5)
matriz1 = [[rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)], [rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)], [rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)]]
np.linalg.det(matriz1)