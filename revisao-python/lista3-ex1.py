### Lista 3 - Exercício 1  ###

import random as rd
print("=" * 5 + "Advinha o Número" + "=" * 5)
numero = rd.randint(0, 10000)
tentativa = int(input("Escreva um número de 0 a 10000: "))
contador = 1

while contador != 11:
    if tentativa < numero:
        print("Tentativa n°{}. Tente um número maior".format(contador))
        tentativa = int(input("Escreva outro número de 0 a 10000: "))
        contador+=1
    elif tentativa > numero:
        print("Tentativa n°{}. Tente um número menor".format(contador))
        tentativa = int(input("Escreva outro número de 0 a 10000: "))
        contador+=1
    else:
        print("Tentativa n°{}. Acertou! A resposta é {}!".format(contador, numero))
        break
else:
    print("Tentativas execidas! Tente na próxima vez.")

