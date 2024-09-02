import numpy as np
import pandas as pd

dados = np.random.uniform(6, 10,  size = (6,10))

df1=pd.DataFrame(dados, index = ['jean', 'felipe', 'andre', 'leandro', 'eduardo', 'juliano'], columns=['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10'])
print(df1)
#print(df1.sum(axis = 1))
#print(df1.sum(axis = 1).idxmin())

print('O campeão foi ', df1.sum(axis = 1).idxmin(), ' que fez ', df1.sum(axis = 1).min(), ' segundos!!!' )