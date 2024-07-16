import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.kdeplot(data=tips, x="total_bill", shade=True)
plt.show()
