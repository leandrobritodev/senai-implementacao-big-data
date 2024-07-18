### Lista 3 - Exercício 2  ###

import random as rd
print("=" * 5 + "Avaliador de Dados" + "=" * 5)
jogadas = int(input("Quantas jogadas deverão ser feitas?: "))
dado2 = 0
dado3 = 0
dado4 = 0
dado5 = 0
dado6 = 0
dado7 = 0
dado8 = 0
dado9 = 0
dado10 = 0
dado11 = 0
dado12 = 0

for i in range(jogadas):
    dados = rd.randint(2,12)
    if dados == 2:
        dado2 += 1
    elif dados == 3:
        dado3 += 1
    elif dados == 4:
        dado4 += 1
    elif dados == 5:
        dado5 += 1
    elif dados == 6:
        dado6 += 1
    elif dados == 7:
        dado7 += 1
    elif dados == 8:
        dado8 += 1
    elif dados == 9:
        dado9 += 1
    elif dados == 10:
        dado10 += 1
    elif dados == 11:
        dado11 += 1
    elif dados == 12:
        dado12 += 1

print('''===== Resultados =====
Soma 2: {} vezes
Soma 3: {} vezes
Soma 4: {} vezes
Soma 5: {} vezes
Soma 6: {} vezes
Soma 7: {} vezes
Soma 8: {} vezes
Soma 9: {} vezes
Soma 10: {} vezes
Soma 11: {} vezes
Soma 12: {} vezes
'''.format(dado2, dado3, dado4, dado5, dado6, dado7, dado8, dado9, dado10, dado11, dado12))