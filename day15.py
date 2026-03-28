import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, classification_report, 
                             confusion_matrix)


# Load and prepare data
df = pd.read_csv("titanic.csv")
df = df[["Survived", "Pclass", "Age", "Fare", "SibSp", "Parch", "Sex"]].dropna()


# Feature engineering
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1


X = df[["Pclass", "Age", "Fare", "Sex", "FamilySize"]]
y = df["Survived"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
plt.imshow(cm, cmap="Blues")
plt.title("Confusion Matrix — Titanic Survival")
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.xticks([0, 1], ["Did not survive", "Survived"])
plt.yticks([0, 1], ["Did not survive", "Survived"])

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", 
                 va="center", color="black", fontsize=14)

plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.close()

print("Confusion Matrix:")
print(cm)
print("\nTrue Negatives:", cm[0][0])
print("False Positives:", cm[0][1])
print("False Negatives:", cm[1][0])
print("True Positives:", cm[1][1])


# Predict survival for new passengers
new_passengers = pd.DataFrame({
    "Pclass": [1, 3],
    "Age": [25, 25],
    "Fare": [100, 8],
    "Sex": [1, 0],
    "FamilySize": [1, 1]
})

predictions = model.predict(new_passengers)
probabilities = model.predict_proba(new_passengers)

passengers_info = ["1st class female, high fare", 
                   "3rd class male, low fare"]

for info, pred, prob in zip(passengers_info, predictions, probabilities):
    outcome = "SURVIVED" if pred == 1 else "DID NOT SURVIVE"
    print(f"{info}")
    print(f"Prediction: {outcome}")
    print(f"Survival probability: {round(prob[1] * 100, 1)}%")
    print("---")