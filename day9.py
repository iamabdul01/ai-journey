import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


df = pd.read_csv("titanic.csv")


# First look at the data
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.isnull().sum())

# clean age data with median
df["Age"] = df["Age"].fillna(df["Age"].median())


#What was the overall survival rate?
#How did gender affect survival?
#How did class affect survival?
#How did age affect survival? (use age groups like Day 6)
#How did family size affect survival?
#What combination of factors gave the BEST chance of survival?
#Build at least 4 charts telling the story visually


# overall survival rate
survival_rate = df["Survived"].mean()
print(f"Overall survival rate: {survival_rate}")


# how gender affected survival
gender = df.groupby("Sex")["Survived"].mean()
print(f"Survival rate by gender:\n{gender}")


# how class affected survival
pclass = df.groupby("Pclass")["Survived"].mean()
print(f"Survival rate by class:\n{pclass}")


# how age affected survival
df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 12, 18, 35, 60, 100], labels=[
                        "Child", "Teen", "Young Adult", "Adult", "Senior"])
print(df.groupby("AgeGroup")["Survived"].mean())


# how family size affected survival
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
print(df.groupby("FamilySize")["Survived"].mean())


# combination of factors for best chance of survival
print(df.groupby(["Sex", "Pclass"])["Survived"].mean())


# charts
# Survival rate by gender
plt.figure()
gender.plot(kind='bar', color=['blue', 'pink'])
plt.ylabel("Survival Rate")
plt.xlabel("Gender")
plt.title("Survival Rate by Gender")
plt.tight_layout()
plt.savefig("Survival_by_Gender.png")
plt.close()


# Survival rate by class
plt.figure()
pclass.plot(kind='bar', color=['gold', 'silver', 'blue'])
plt.ylabel("Survival Rate")
plt.xlabel("Class")
plt.title("Survival Rate by Class")
plt.tight_layout()
plt.savefig("Survival_by_Class.png")
plt.close()


# Survival rate by age group
plt.figure()
age_group = df.groupby("AgeGroup")["Survived"].mean()
age_group.plot(kind='bar', color='lightblue')
plt.ylabel("Survival Rate")
plt.xlabel("Age Group")
plt.title("Survival Rate by Age Group")
plt.tight_layout()
plt.savefig("Survival_by_AgeGroup.png")
plt.close()


# Survival rate by family size
plt.figure()
family_size = df.groupby("FamilySize")["Survived"].mean()
family_size.plot(kind='bar', color='lightcoral')
plt.ylabel("Survival Rate")
plt.xlabel("Family Size")
plt.title("Survival Rate by Family Size")
plt.tight_layout()
plt.savefig("Survival_by_FamilySize.png")
plt.close()

print("All charts saved!")

