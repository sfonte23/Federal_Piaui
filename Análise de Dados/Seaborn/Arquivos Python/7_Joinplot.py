import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter")
plt.show()
