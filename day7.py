<<<<<<< HEAD
import pandas as pd
import numpy as np


# Simulate two separate datasets that need to be merged
fighters = pd.DataFrame({
    "fighter_id": [1, 2, 3, 4, 5],
    "name": ["Abdul", "Fighter2", "Fighter3", "Fighter4", "Fighter5"],
    "age": [25, 30, 22, 28, None],
    "weight": [75, 80, None, 70, 85]
})


stats = pd.DataFrame({
    "fighter_id": [1, 2, 3, 4, 6],
    "wins": [10, 8, 15, 5, 12],
    "losses": [2, 3, 1, 7, 4],
    "rank": ["A", "B", "S", "C", None]
})


# print("Fighters dataset:")
# print(fighters)
# print("\nStats dataset:")
# print(stats)


# Merge the two datasets
merged = pd.merge(fighters, stats, on="fighter_id", how="left")
# print("\nMerged dataset:")
# print(merged)


# Check for missing values
# print(merged.isnull().sum())


# Fill missing numerical values with median
merged["age"] = merged["age"].fillna(merged["age"].median())
merged["weight"] = merged["weight"].fillna(merged["weight"].median())
merged["wins"] = merged["wins"].fillna(0)
merged["losses"] = merged["losses"].fillna(0)


# Fill missing rank with unranked
merged["rank"] = merged["rank"].fillna("unranked")


# Check again - should all be zeros now
# print(merged.isnull().sum())
# print(merged)


# remove duplicates - important in real world data
merged = merged.drop_duplicates()
# print("Shape after dropping duplicates:", merged.shape)


# Rename columns for clarity
merged = merged.rename(columns={"fighter_id": "id", "rank": "tier"})
# print(merged.columns.tolist())


# Calculate a new column called "win_rate"
# win_rate = wins / (wins + losses)
# If wins + losses = 0, win_rate should be 0 (avoid dividing by zero)


merged["win_rate"] = merged.apply(lambda row: 0 if (
    row["wins"] + row["losses"]) == 0 else row["wins"] / (row["wins"] + row["losses"]), axis=1)
print(merged)
=======
import pandas as pd
import numpy as np


# Simulate two separate datasets that need to be merged
fighters = pd.DataFrame({
    "fighter_id": [1, 2, 3, 4, 5],
    "name": ["Abdul", "Fighter2", "Fighter3", "Fighter4", "Fighter5"],
    "age": [25, 30, 22, 28, None],
    "weight": [75, 80, None, 70, 85]
})


stats = pd.DataFrame({
    "fighter_id": [1, 2, 3, 4, 6],
    "wins": [10, 8, 15, 5, 12],
    "losses": [2, 3, 1, 7, 4],
    "rank": ["A", "B", "S", "C", None]
})


# print("Fighters dataset:")
# print(fighters)
# print("\nStats dataset:")
# print(stats)


# Merge the two datasets
merged = pd.merge(fighters, stats, on="fighter_id", how="left")
# print("\nMerged dataset:")
# print(merged)


# Check for missing values
# print(merged.isnull().sum())


# Fill missing numerical values with median
merged["age"] = merged["age"].fillna(merged["age"].median())
merged["weight"] = merged["weight"].fillna(merged["weight"].median())
merged["wins"] = merged["wins"].fillna(0)
merged["losses"] = merged["losses"].fillna(0)


# Fill missing rank with unranked
merged["rank"] = merged["rank"].fillna("unranked")


# Check again - should all be zeros now
# print(merged.isnull().sum())
# print(merged)


# remove duplicates - important in real world data
merged = merged.drop_duplicates()
# print("Shape after dropping duplicates:", merged.shape)


# Rename columns for clarity
merged = merged.rename(columns={"fighter_id": "id", "rank": "tier"})
# print(merged.columns.tolist())


# Calculate a new column called "win_rate"
# win_rate = wins / (wins + losses)
# If wins + losses = 0, win_rate should be 0 (avoid dividing by zero)


merged["win_rate"] = merged.apply(lambda row: 0 if (
    row["wins"] + row["losses"]) == 0 else row["wins"] / (row["wins"] + row["losses"]), axis=1)
print(merged)
>>>>>>> 2bc073d92990917a456f9e8034dd73cce3eae219
