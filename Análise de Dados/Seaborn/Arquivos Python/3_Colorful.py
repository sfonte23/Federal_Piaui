import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set_palette("pastel")
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()