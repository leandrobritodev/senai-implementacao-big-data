import pandas as pd
import numpy as np

matriz = np.random.uniform(10, 6, size=(10,6))
matrizT = matriz.T

dados = {'Ayrton Senna':[matriz[0][0], matriz[1][0], matriz[2][0], matriz[3][0], matriz[4][0], matriz[5][0], matriz[6][0], matriz[7][0], matriz[8][0], matriz[9][0]],
         "Felipe Massa":[matriz[0][1], matriz[1][1], matriz[2][1], matriz[3][1], matriz[4][1], matriz[5][1], matriz[6][1], matriz[7][1], matriz[8][1], matriz[9][1]],
         "Emerson Fittipaldi":[matriz[0][2], matriz[1][2], matriz[2][2], matriz[3][2], matriz[4][2], matriz[5][2], matriz[6][2], matriz[7][2], matriz[8][2], matriz[9][2]],
         "Rubens Barrichello":[matriz[0][3], matriz[1][3], matriz[2][3], matriz[3][3], matriz[4][3], matriz[5][3], matriz[6][3], matriz[7][3], matriz[8][3], matriz[9][3]],
         "Leandro Brito":[matriz[0][4], matriz[1][4], matriz[2][4], matriz[3][4], matriz[4][4], matriz[5][4], matriz[6][4], matriz[7][4], matriz[8][4], matriz[9][4]],
         "Jean Justino":[matriz[0][5], matriz[1][5], matriz[2][5], matriz[3][5], matriz[4][5], matriz[5][5], matriz[6][5], matriz[7][5], matriz[8][5], matriz[9][5]]}

df1 = pd.DataFrame(dados)
df1.index = ["volta 1", "volta 2", "volta 3", "volta 4", "volta 5", "volta 6", "volta 7", "volta 8", "volta 9", "volta 10"]

print(df1)

# Soma dos tempos
somas = np.sum(df1, axis = 0)
print('o argmin é : ', np.argmin(somas))
print('o min é : ',np.min(somas))

# Ordem de chegada
ordem = df1.columns[np.argmin(somas)]

print('O campeao foi o corredor: ' + df1.columns[(np.argmin(somas))] + ' que fez : ' + str(np.min(somas)) + ' segundos em toda a prova!!!!')

print(somas)
