import pandas as pd
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


df = pd.read_csv("titanic.csv")


# Split passengers into survivors and non-survivors
survivors = df[df["Survived"] == 1]["Fare"]
non_survivors = df[df["Survived"] == 0]["Fare"]


# Compare means
#print("Mean fare - Survived:", round(survivors.mean(), 2))
#print("Mean fare - Non-Survived:", round(non_survivors.mean(), 2))


# T-test - did fare ACTUALLY affect survival or was it just random chance?
t_stat, p_value = stats.ttest_ind(survivors, non_survivors)
#print("T-statistic:", round(t_stat, 4))
#print("P-value:", round(p_value, 4))


#if p_value < 0.05:
    #print("The difference in fares between survivors and non-survivors is statistically significant.")
    #print("Fare genuinely affected survival - not random chance")
#else:    
    #print("RESULT: The difference could be random chance.")


# Did age affect survival?
survived_age = df[df["Survived"] == 1]["Age"].dropna()
not_survived_age = df[df["Survived"] == 0]["Age"].dropna()

#print("Mean age — Survived:", round(survived_age.mean(), 2))
#print("Mean age — Not Survived:", round(not_survived_age.mean(), 2))

t_stat, p_value = stats.ttest_ind(survived_age, not_survived_age)
#print("P-value:", round(p_value, 4))

#if p_value < 0.05:
    #print("RESULT: Age significantly affected survival!")
#else:
    #print("RESULT: Age difference could be random chance.")


# Summary of what actually drove survival
features = ["Pclass", "Age", "Fare", "SibSp", "Parch"]

print("Feature correlations with Survival:")
for feature in features:
    corr = df["Survived"].corr(df[feature])
    p = stats.ttest_ind(
        df[df["Survived"]==1][feature].dropna(),
        df[df["Survived"]==0][feature].dropna()
    )[1]
    significance = "✅ Significant" if p < 0.05 else "❌ Not significant"
    print(f"{feature}: correlation={round(corr,3)}, p-value={round(p,4)} — {significance}")