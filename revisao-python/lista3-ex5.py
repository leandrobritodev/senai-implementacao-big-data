### Lista 3 - Exercício 5  ###

import random as rd
import time
print("=" * 5 + "Jogo da Forca" + "=" * 5)
time.sleep(1)
segredo = "capivara"
tentativa = 0
print("Descubra qual é a palavra secreta!")
time.sleep(1)
print("Você tem 10 tentativas!")
for i in range(10):
  tentativa += 1
  teclado = input("Tentativa n°" + str(tentativa) + ": ")
  if teclado == segredo:
    print("Parabéns! Você acertou")
    break
  else:
    print("Errou! Tente outra vez!")
    continue
else:
  print("Acabaram as tentativas!")
