import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('Agg')

df = pd.read_csv("titanic.csv")

# Chart 1 — Survival count
plt.figure()
df["Survived"].value_counts().plot(kind="bar", color=["red", "green"])
plt.title("Titanic Survival Count")
plt.xlabel("Survived (0=No, 1=Yes)")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("survival_count.png")
plt.close()

# Chart 2 — Survival rate by gender
plt.figure()
df.groupby("Sex")["Survived"].mean().plot(kind="bar", color=["blue", "pink"])
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.tight_layout()
plt.savefig("survival_by_gender.png")
plt.close()

# Chart 3 — Survival rate by class
plt.figure()
df.groupby("Pclass")["Survived"].mean().plot(
    kind="bar", color=["gold", "silver", "brown"])
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.tight_layout()
plt.savefig("survival_by_class.png")
plt.close()

# Chart 4 — Age distribution
plt.figure()
df["Age"].fillna(df["Age"].median()).plot(
    kind="hist", bins=30, color="steelblue", edgecolor="black")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("age_distribution.png")
plt.close()

print("All charts saved!")
