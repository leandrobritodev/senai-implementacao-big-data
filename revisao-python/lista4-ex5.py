### Lista 4 - Exercício 5  ###

import time
print("=" * 5 + "Texto bagunçadão" + "=" * 5)
time.sleep(1)
texto = input("Digite o texto: ")

def invertexto(texto):
  for i in range(len(texto)):
    print(texto[len(texto[:-3]+texto[-3:]) - i - 1], end="")

print(invertexto(texto))