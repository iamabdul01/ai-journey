import pandas as pd

# Creating a DataFrame — think of it as a super powered Excel table
data = {
    "name": ["Abdul", "Fighter2", "Fighter3", "Fighter4"],
    "speed": [85, 72, 90, 65],
    "strength": [90, 88, 75, 95],
    "defense": [70, 85, 80, 60]
}

df = pd.DataFrame(data)

print(df)
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.describe())

# Selecting specific columns
print(df["speed"])
print(df[["name", "strength"]])

# Filtering rows — like a database query
fast_fighters = df[df["speed"] > 75]
print(fast_fighters)

# Adding a new column
df["total"] = df["speed"] + df["strength"] + df["defense"]
print(df)

# Sorting
print(df.sort_values("total", ascending=False))