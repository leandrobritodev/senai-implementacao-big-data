### Lista 3 - Exercício 4  ###

import random as rd
import time
print("=" * 5 + "Combate Insano" + "=" * 5)
time.sleep(1)
vida_player = 10
vida_maquina = 10

while vida_maquina > 0:
  print("====== Pontos de Vida ======")
  print("Você: {} | Máquina: {}".format(vida_player, vida_maquina))
  print("============================")
  time.sleep(1)
  print("Escolha um ataque ou digite I para informações")
  time.sleep(1)
  print("A --> Cabeçada")
  time.sleep(1)
  print("B --> Soco")
  time.sleep(1)
  decisao = input("Opção: ").upper()
  if decisao not in ("A", "B", "I"):
        print("Escolha inválida! As opções são 'A', 'B' ou 'I' ")
        time.sleep(1)
        continue
  elif decisao == "I":
    print("Cabeçada: 3 (Poder de combate) | 3 (Força) | 1 (Dano)")
    print("Soco: D6 (Poder de combate) | D6 (Força) ")
    time.sleep(1)
    decisao = input("Opção: ").upper()
  elif decisao == "A":
    dado_player = rd.randint(1,6)
    dado_maquina = rd.randint(1,6)
    if dado_player > 3:
      vida_maquina -= 3
      vida_player -= 1
      time.sleep(1)
    else:
      vida_player -= dado_maquina
      time.sleep(1)
  elif decisao == "B":
    dado_player = rd.randint(1,6)
    dado_maquina = rd.randint(1,6)
    if dado_maquina > dado_player:
      vida_player -= dado_maquina
      time.sleep(1)
    else:
      vida_maquina -= dado_player
      time.sleep(1)
  if vida_player < 1:
    print("Derrota!")
    time.sleep(1)
    print("====== Pontos de Vida ======")
    print("Você: {} | Máquina: {}".format(vida_player, vida_maquina))
    print("============================")
    time.sleep(1)
    break

else:
  print("Vitória!!!!")
  print("====== Pontos de Vida ======")
  print("Você: {} | Máquina: {}".format(vida_player, vida_maquina))
  print("============================")
  time.sleep(1)