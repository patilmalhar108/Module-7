import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("USA_Housing.csv")
print(df.head(10))
print(df.info())
print(df.describe())
sns.pairplot(df.select_dtypes(include = [np.number]))
sns.heatmap(df.select_dtypes(include = [np.number]).corr(), annot = True)
plt.show()