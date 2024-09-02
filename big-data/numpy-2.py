# Corrida maluca

import numpy as np

dados = np.random.uniform(10, 6,  size = (10,6))
dadosT = dados.T


print(dados)
print('essa é a matriz transposta: ')
print(dadosT)


print('a lista de soma de dados: ')
print(np.sum(dados, axis = 0))

print(np.sum(dadosT, axis = 1))

somas = np.sum(dados, axis = 0)
print('o argmin é : ', np.argmin(somas))
print('o min é : ',np.min(somas))

print('O campeao foi o corredor: ' + str(np.argmin(somas) + 1) + ' que fez : ' + str(np.min(somas)) + ' segundos em toda a prova!!!!')