import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.boxplot(data=tips, x="day", y="total_bill")
plt.show()
