### Lista 4 - Exercício 2  ###

import time
print("=" * 5 + "Apelidos Maneiros" + "=" * 5)
time.sleep(1)
nome = input("Digite  seu nome: ")
sobrenome = input("Digite  seu sobrenome: ")

def apelido(nome, sobrenome):
  return str(nome[:3])+(sobrenome[-3:])

print(apelido(nome, sobrenome))