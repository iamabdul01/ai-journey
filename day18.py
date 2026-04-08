import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import accuracy_score

# Load and prepare data
df = pd.read_csv("titanic.csv")
df = df[["Survived", "Pclass", "Age",
         "Fare", "SibSp", "Parch", "Sex"]].dropna()

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

X = df[["Pclass", "Age", "Fare", "Sex", "FamilySize"]]
y = df["Survived"]

# Cross validation on all 3 models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

print("--- 5-Fold Cross Validation Results ---")
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    print(f"{name}:")
    print(f"  Scores: {[round(s*100, 1) for s in scores]}")
    print(f"  Mean: {round(scores.mean()*100, 2)}%")
    print(f"  Std Dev: {round(scores.std()*100, 2)}%")


    from sklearn.model_selection import GridSearchCV

# Define parameters to try
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 4, 5, None],
    "min_samples_split": [2, 5, 10]
}

# Grid search finds the best combination
rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(rf, param_grid, cv=5, 
                           scoring="accuracy", verbose=1)
grid_search.fit(X, y)

print("Best parameters:", grid_search.best_params_)
print("Best cross val score:", 
      round(grid_search.best_score_ * 100, 2), "%")


# Train final tuned model
best_rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    min_samples_split=5,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

best_rf.fit(X_train, y_train)
y_pred = best_rf.predict(X_test)

print("Final Tuned Model Accuracy:", 
      round(accuracy_score(y_test, y_pred) * 100, 2), "%")

# Feature importance
print("\nFeature Importance:")
for feature, importance in sorted(
    zip(X.columns, best_rf.feature_importances_),
    key=lambda x: x[1], reverse=True
):
    bar = "█" * int(importance * 50)
    print(f"{feature:12} {bar} {round(importance * 100, 1)}%")