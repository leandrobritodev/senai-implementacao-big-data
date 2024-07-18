### Lista 3 - Exercício 3  ###

import random as rd
import time
print("=" * 5 + "Trocação de Tiro" + "=" * 5)
time.sleep(1)
print("Você está na favela da facção rival e encontrou um traficante, que começou um tiroteio com você.")
time.sleep(1)
vida_player = 10
vida_maquina = 10

while True:
    print("Fiel: {} | Alemão: {}".format(vida_player, vida_maquina))
    time.sleep(1)
    print('''Escolha um ataque ou digite I para informações
A --> Rajadão
B --> Glokzada''')
    time.sleep(1)
    escolha = input("Escolha: ").upper()
    if escolha not in ("A", "B", "I"):
        print("Escolha inválida\n")
        time.sleep(1)
        continue
    elif escolha == "I":
        print('''A --> Rajadão (Poder de combate: +3 | Dano: -1)
B --> Glokzada (Poder de combate: aleatório(rolar o D6))''')
        time.sleep(3)
        continue
    elif escolha == "A":
        continue
    