
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ppm_dummy_data.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
df.info()

print(df["Current_Payment"].value_counts())

sns.countplot(x="Current_Payment", data=df)
plt.show()

missing = df.isnull().sum()
missing = missing[missing > 0]
print(missing.sort_values(ascending=False).head(20))

print(df["Age"].describe())
sns.histplot(df["Age"])
plt.show()

print(df["Balance"].describe())
sns.histplot(df["Balance"])
plt.show()

print(df["Deliquency"].value_counts())
sns.countplot(x="Deliquency", data=df)
plt.show()

print(df["Previous_Payment"].value_counts())

print(df.groupby("Current_Payment")["Balance"].mean())
print(df.groupby("Current_Payment")["Deliquency"].mean())
print(df.groupby("Current_Payment")["Age"].mean())

print(df["Recency"].describe())
sns.boxplot(x="Current_Payment", y="Recency", data=df)
plt.show()

corr = df[["Balance", "Deliquency", "Recency", "Age", "Current_Payment"]].corr()
print(corr)

sns.heatmap(corr, annot=True)
plt.show()
sns.heatmap(corr, annot=True)
plt.show()
