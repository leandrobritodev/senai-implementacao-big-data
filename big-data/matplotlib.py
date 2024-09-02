import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dados = np.random.uniform(6, 10, size=(6, 10))

df1 = pd.DataFrame(dados, index = ['Ayrton Senna', 'Felipe Massa', 'Emerson Fittipaldi', 'Rubens Barrichello', 'Leandro Brito', 'Jean Justino'],
                   columns=['volta 1', 'volta 2', 'volta 3', 'volta 4', 'volta 5', 'volta 6', 'volta 7', 'volta 8', 'volta 9', 'volta 10'])

plot = df1.plot.bar(y='volta 8', figsize=(6,4), ylim=(6, 10))
plt.xlabel('Pilotos')
plt.ylabel('Segundos')
plt.title('Tempo dos pilotos na Volta 8')