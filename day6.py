import pandas as pd

df = pd.read_csv("titanic.csv")

# GroupBy - split data into groups and analyze each group
# print(df.groupby("Sex")["Fare"].mean())
# print(df.groupby("Pclass")["Age"].mean())


# GroupBy - multiply columns at once
# print(df.groupby(["Sex", "Pclass"])["Survived"].mean())


# Value counts with normalize - shows percentages
# print(df["Pclass"].value_counts(normalize=True))


# Sorting values
# print(df.sort_values("Fare", ascending=False).head(10))


# Creating new columns from existing data
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)


# Did traveling alone affect survival?
print(df.groupby("IsAlone")["Survived"].mean())


# Age goroups - binning data
df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 12, 18, 35, 60, 100], labels=[
                        "Child", "Teen", "Young Adult", "Adult", "Senior"])
print(df.groupby("AgeGroup")["Survived"].mean())
