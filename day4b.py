import pandas as pd

# Load the real dataset
df = pd.read_csv("titanic.csv")

# First look at the data
print(df.shape)
print(df.head())
print(df.columns.tolist())
print(df.describe())
print(df.isnull().sum())


# How many people survived?
print(df["Survived"].value_counts())

# Survival rate by gender
print(df.groupby("Sex")["Survived"].mean())

# Survival rate by passenger class
print(df.groupby("Pclass")["Survived"].mean())

# Average age of survivors vs non survivors
print(df.groupby("Survived")["Age"].mean())

# Fix missing age — replace with median age
df["Age"] = df["Age"].fillna(df["Age"].median())
print(df.isnull().sum())