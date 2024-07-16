import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(data=tips, x="total_bill")
plt.show()
