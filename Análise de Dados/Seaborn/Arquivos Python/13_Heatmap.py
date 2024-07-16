import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
tips = sns.load_dataset("tips")
print(tips.head())  # Verifique se o dataset foi carregado corretamente

# Calcular a matriz de correlação
corr = tips.corr()
print(corr)  # Verifique a matriz de correlação

# Criar o heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm")

# Exibir o gráfico
plt.show()
