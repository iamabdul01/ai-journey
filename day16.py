import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load and prepare data
df = pd.read_csv("titanic.csv")
df = df[["Survived", "Pclass", "Age",
         "Fare", "SibSp", "Parch", "Sex"]].dropna()

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

X = df[["Pclass", "Age", "Fare", "Sex", "FamilySize"]]
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Decision Tree
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)

# Evaluate
y_pred = tree.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Decision Tree Accuracy:", round(accuracy * 100, 2), "%")

# Print the tree structure
tree_rules = export_text(tree, feature_names=list(X.columns))
print("\nDecision Tree Rules (first few levels):")
print('\n'.join(tree_rules.split('\n')[:20]))


# Check overfitting
train_pred = tree.predict(X_train)
train_accuracy = accuracy_score(y_train, train_pred)
test_accuracy = accuracy_score(y_test, y_pred)

print("Training accuracy:", round(train_accuracy * 100, 2), "%")
print("Test accuracy:", round(test_accuracy * 100, 2), "%")
print("Difference:", round((train_accuracy - test_accuracy) * 100, 2), "%")

# How deep is the tree?
print("Tree depth:", tree.get_depth())
print("Number of leaves:", tree.get_n_leaves())


# Fix overfitting by limiting tree depth
tree_fixed = DecisionTreeClassifier(max_depth=4, random_state=42)
tree_fixed.fit(X_train, y_train)

train_pred_fixed = tree_fixed.predict(X_train)
test_pred_fixed = tree_fixed.predict(X_test)

train_acc = accuracy_score(y_train, train_pred_fixed)
test_acc = accuracy_score(y_test, test_pred_fixed)

print("Fixed Tree Results:")
print("Training accuracy:", round(train_acc * 100, 2), "%")
print("Test accuracy:", round(test_acc * 100, 2), "%")
print("Difference:", round((train_acc - test_acc) * 100, 2), "%")
print("Tree depth:", tree_fixed.get_depth())
print("Number of leaves:", tree_fixed.get_n_leaves())

# Compare all models so far
print("\n--- Model Comparison ---")
print(f"Logistic Regression:     74.13%")
print(f"Decision Tree (deep):    73.43%")
print(f"Decision Tree (depth=4): {round(test_acc * 100, 2)}%")