import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# Load titanic
df = pd.read_csv("titanic.csv")

# Select features
df = df[["Survived", "Pclass", "Age", "Fare", "SibSp", "Parch"]].dropna()

X = df[["Pclass", "Age", "Fare", "SibSp", "Parch"]]
y = df["Survived"]


# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#print("Training set size:", X_train.shape)
#print("Test set size:", X_test.shape)


# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

#print(f"Mean Squared Error: {round(mse, 4)}")
#print(f"Root Mean Squared Error: {round(rmse, 4)}")
#print(f"R^2 Score: {round(r2, 4)}")

# feature importance
#print("\nFeature Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f" {feature}: {round(coef, 4)}")
#print(f" Intercept: {round(model.intercept_, 4)}")


# Visualize predicted vs actual
#plt.figure()
#plt.scatter(y_test, y_pred, alpha=0.5, color="steelblue")
#plt.axhline(y=0.5, color="red", linestyle="--", label="Decision boundary")
#plt.xlabel("Actual Survival (0 or 1)")
#plt.ylabel("Predicted Value")
#plt.title("Linear Regression — Predicted vs Actual Survival")
#plt.legend()
#plt.tight_layout()
#plt.savefig("predictions_vs_actual.png")
#plt.close()

# Visualize predicted vs actual
#plt.figure()
#plt.scatter(y_test, y_pred, alpha=0.5, color="steelblue")
#plt.axhline(y=0.5, color="red", linestyle="--", label="Decision boundary")
#plt.xlabel("Actual Survival (0 or 1)")
#plt.ylabel("Predicted Value")
#plt.title("Linear Regression — Predicted vs Actual Survival")
#plt.legend()
#plt.tight_layout()
#plt.savefig("predictions_vs_actual.png")
#plt.close()


# visualize predicted vs actual
#plt.figure()
#plt.scatter(y_test, y_pred, alpha=0.5, color="steelblue")
#plt.axhline(y=0.5, color="red", linestyle="--", label="Decision boundary")
#plt.xlabel("Actual Survival (0 or 1)")
#plt.ylabel("Predicted Value")
#plt.title("Linear Regression — Predicted vs Actual Survival")
#plt.legend()
#plt.tight_layout()
#plt.savefig("predictions_vs_actual.png")
#plt.close()



# show where model goes wrong
above = y_pred[y_pred > 1]
below = y_pred[y_pred < 0]
#print(f"Predictions above 1: {len(above)}")
#print(f"Predictions below 0: {len(below)}")
#print(f"This proves linear regression is wrong for classification!")


# Encode Sex column — convert text to numbers
df2 = pd.read_csv("titanic.csv")
df2 = df2[["Survived", "Pclass", "Age", 
            "Fare", "SibSp", "Parch", "Sex"]].dropna()

# Convert male/female to 0/1
df2["Sex"] = df2["Sex"].map({"male": 0, "female": 1})

# Add FamilySize feature
df2["FamilySize"] = df2["SibSp"] + df2["Parch"] + 1

X2 = df2[["Pclass", "Age", "Fare", "Sex", "FamilySize"]]
y2 = df2["Survived"]

X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X2, y2, test_size=0.2, random_state=42
)

model2 = LinearRegression()
model2.fit(X_train2, y_train2)
y_pred2 = model2.predict(X_test2)

r2_new = r2_score(y_test2, y_pred2)
print("Old R² (without Sex & FamilySize):", 0.1661)
print("New R² (with Sex & FamilySize):", round(r2_new, 4))
print("Improvement:", round((r2_new - 0.1661) * 100, 1), "%")