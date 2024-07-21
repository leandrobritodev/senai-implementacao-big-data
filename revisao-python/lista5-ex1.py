### Lista 4 - Exercício 5  ###

import time
print("=" * 5 + "Dados com Índices" + "=" * 5)
time.sleep(1)
nomes = ["jose", "jorge", "maria", "antonio", "ana", "julia", "marcio", "fernando", "zelia"]
for i in range(len(nomes)):
  print(i+1, "-" , nomes[i])