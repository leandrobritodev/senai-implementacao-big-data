### Lista 4 - Exercício 1  ###

import time
print("=" * 5 + "Pokedex" + "=" * 5)
time.sleep(1)
nome = input("Digite o seu nome: ")

def pokedex(nome):
  return str(nome[:4]) + "mon"

print("Seu nome é ", pokedex(nome))