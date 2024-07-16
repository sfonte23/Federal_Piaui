import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.barplot(data=tips, x="day", y="total_bill")
plt.show()
