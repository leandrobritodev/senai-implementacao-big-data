### Lista 4 - Exercício 4  ###

import time
print("=" * 5 + "Invertexto" + "=" * 5)
time.sleep(1)
texto = input("Digite o texto: ")

def invertexto(texto):
  for i in range(len(texto)):
    print(texto[len(texto) - i - 1], end="")

print(invertexto(texto))