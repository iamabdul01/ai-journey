import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Create simple dataset - hours studied vs exam score
np.random.seed(42)
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
scores = np.array([52, 58, 65, 70, 75, 82, 88, 92, 96, 99], dtype=float )


# Visualise the data first
#plt.figure()
#plt.scatter(hours, scores, color="steelblue", s=100)
#plt.xlabel("Hours Studied")
#plt.ylabel("Exam Score")
#plt.title("Hours Studied vs Exam Score")
#plt.tight_layout()
#plt.savefig("study_data.png")
#plt.close()


#print("Hours:", hours)
#print("Scores:", scores)


# Linear Regression from scratch using Gradient Descent
# Step 1 — Initialize parameters
m = 0.0  # slope
b = 0.0  # intercept
learning_rate = 0.01
epochs = 1000
n = len(hours)

# Step 2 — Training loop
loss_history = []

for epoch in range(epochs):
    # Forward pass — make predictions
    predictions = m * hours + b
    
    # Calculate loss (Mean Squared Error)
    loss = (1/n) * np.sum((predictions - scores) ** 2)
    loss_history.append(loss)
    
    # Calculate gradients
    dm = (2/n) * np.sum((predictions - scores) * hours)
    db = (2/n) * np.sum(predictions - scores)
    
    # Update parameters
    m = m - learning_rate * dm
    b = b - learning_rate * db
    
    # Print progress every 200 epochs
    if epoch % 200 == 0:
        print(f"Epoch {epoch}: Loss={round(loss, 2)}, m={round(m, 3)}, b={round(b, 3)}")

print(f"\nFinal slope (m): {round(m, 3)}")
print(f"Final intercept (b): {round(b, 3)}")
print(f"Final loss: {round(loss_history[-1], 2)}")


# Plot 1 — Loss curve
plt.figure()
plt.plot(loss_history, color="red")
plt.title("Loss Over Time — Gradient Descent")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.tight_layout()
plt.savefig("loss_curve.png")
plt.close()

# Plot 2 — Regression line vs actual data
plt.figure()
plt.scatter(hours, scores, color="steelblue", s=100, label="Actual")
predicted_line = m * hours + b
plt.plot(hours, predicted_line, color="red", linewidth=2, label="Predicted")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Linear Regression — Hours vs Score")
plt.legend()
plt.tight_layout()
plt.savefig("regression_line.png")
plt.close()

# Make new predictions
test_hours = np.array([3.5, 6.5, 11])
test_predictions = m * test_hours + b
for h, p in zip(test_hours, test_predictions):
    print(f"Hours studied: {h} → Predicted score: {round(p, 1)}")