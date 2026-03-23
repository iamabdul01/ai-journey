import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


df = pd.read_csv("titanic.csv")


# Central tendency
#print("Mean age:", df["Age"].mean())
#print("Median age:", df["Age"].median())
#print("Mode age:", df["Age"].mode()[0])


# Spread
#print("Std deviation:", df["Age"].std())
#print("Variance:", df["Age"].var())
#print("Range:", df["Age"].max() - df["Age"].min())


# Correlation matrix
#print(df[["Survived", "Pclass", "Age", "Fare", "SibSp", "Parch"]].corr())


# Correlation heatmap
#plt.figure(figsize=(8, 6))
#corr = df[["Survived", "Pclass", "Age", "Fare", "SibSp", "Parch"]].corr()
#sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
#plt.title("Correlation Heatmap - Titanic Dataset")
#plt.tight_layout()
#plt.savefig("titanic_correlation_heatmap.png")
#plt.close()


#print("Heatmap saved!")


# Normal distribution — the most important distribution in ML
from scipy import stats

# Generate a normal distribution
np.random.seed(42)
normal_data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure()
plt.hist(normal_data, bins=30, edgecolor="black", color="steelblue")
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("normal_distribution.png")
plt.close()

# Key stats
print("Mean:", round(np.mean(normal_data), 2))
print("Std Dev:", round(np.std(normal_data), 2))
print("% of data within 1 std dev:", 
      round(np.mean(np.abs(normal_data) < 1) * 100, 1), "%")
print("% of data within 2 std dev:", 
      round(np.mean(np.abs(normal_data) < 2) * 100, 1), "%")
