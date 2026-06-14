import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv("ppm_dummy_data.csv")
df.head()
# size of data
df.shape
# check columns 
df.columns.tolist()
# datatypes
df.info()
df["Current_Payment"].value_counts()
# visualize
sns.countplot(x="Current_Payment", data=df)
plt.show()
# find missing values
missing = df.isnull().sum()
missing = missing[missing > 0]
missing.sort_values(
    ascending=False
).head(20)
df["Age"].describe()
sns.histplot(df["Age"])
plt.show()
df["Balance"].describe()
sns.histplot(df["Balance"])
plt.show()
