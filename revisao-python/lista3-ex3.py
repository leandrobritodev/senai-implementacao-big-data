### Lista 3 - Exercício 3  ###

import random as rd
import time
print("=" * 5 + "Padra Pepel e Tasoure" + "=" * 5)
time.sleep(1)
print("Digite Papel(P), Pedra(R) ou Tesoura(T), aperte X para sair")
time.sleep(1)

vitorias = 0
derrotas = 0
empates = 0

while True:
    jogada = input("Faça sua jogada: ").upper()
    computador = rd.randint(1,3)
    time.sleep(1)

    #Validação das Escolhas
    if jogada not in ("P", "R", "T", "X"):
        print("Jogada inválida\n")
        time.sleep(1)
        continue
    elif jogada == "X":
        print('''==== Saindo do jogo ====
Resultado final:
Vitórias: {}
Derrotas: {}
Empates: {}'''.format(vitorias, derrotas, empates))
        time.sleep(2)
        break
    elif jogada == "P" and computador == 2:
        print("Venceu! O sistema escolheu pedra.")
        time.sleep(0.5)
        vitorias = vitorias + 1
        print("Vitórias: {}| Derrotas: {}| Empates: {}".format(vitorias, derrotas, empates))
        continue
    elif jogada == "P" and computador == 3:
        print("Perdeu! O sistema escolheu tesoura.")
        time.sleep(0.5)
        derrotas = derrotas + 1
        print("Vitórias: {}| Derrotas: {}| Empates: {}".format(vitorias, derrotas, empates))
        continue
    elif jogada == "P" and computador == 1:
        print("Empate! O sistema escolheu papel também.")
        time.sleep(0.5)
        empates = empates + 1
        print("Vitórias: {}| Derrotas: {}| Empates: {}".format(vitorias, derrotas, empates))
        continue
    elif jogada == "R" and computador == 3:
        print("Venceu! O sistema escolheu tesoura.")
        time.sleep(0.5)
        vitorias = vitorias + 1
        print("Vitórias: {}| Derrotas: {}| Empates: {}".format(vitorias, derrotas, empates))
        continue
    elif jogada == "R" and computador == 1:
        print("Perdeu! O sistema escolheu papel.")
        time.sleep(0.5)
        derrotas = derrotas + 1
        print("Vitórias: {}| Derrotas: {}| Empates: {}".format(vitorias, derrotas, empates))
        continue
    elif jogada == "R" and computador == 2:
        print("Empate! O sistema escolheu pedra também.")
        time.sleep(0.5)
        empates = empates + 1
        print("Vitórias: {}| Derrotas: {}| Empates: {}".format(vitorias, derrotas, empates))
        continue
    elif jogada == "T" and computador == 1:
        print("Venceu! O sistema escolheu papel.")
        time.sleep(0.5)
        vitorias = vitorias + 1
        print("Vitórias: {}| Derrotas: {}| Empates: {}".format(vitorias, derrotas, empates))
        continue
    elif jogada == "T" and computador == 2:
        print("Perdeu! O sistema escolheu pedra.")
        time.sleep(0.5)
        derrotas = derrotas + 1
        print("Vitórias: {}| Derrotas: {}| Empates: {}".format(vitorias, derrotas, empates))
        continue
    elif jogada == "T" and computador == 3:
        print("Empate! O sistema escolheu tesoura também.")
        time.sleep(0.5)
        empates = empates + 1
        print("Vitórias: {}| Derrotas: {}| Empates: {}".format(vitorias, derrotas, empates))
        continue
    