import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Relação entre Total da Conta e Gorjeta")
plt.xlabel("Total da Conta")
plt.ylabel("Gorjeta")
plt.show()
