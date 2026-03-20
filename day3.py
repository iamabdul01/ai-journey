<<<<<<< HEAD
import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

# Plain Python list
my_list = [1, 2, 3, 4, 5]
print(my_list * 2)

# Basic operations
print(arr1 + arr2)
print(arr1 * 2)
print(arr2 / 10)

# Useful stats
print(np.mean(arr1))
print(np.max(arr2))
print(np.min(arr1))
print(np.sum(arr1))

# 2D arrays (this is how ML data actually looks)
data = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80]
])

print("Shape:", data.shape)
print("Rows:", data.shape[0])
print("Columns:", data.shape[1])

# Math on the whole table at once
print("Mean of each column:", np.mean(data, axis=0))
print("Mean of each row:", np.mean(data, axis=1))

# Slicing — grabbing specific data
print("First row:", data[0])
print("Last column:", data[:, 2])
print("One specific value:", data[1, 2])
=======
import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

# Basic operations
print(arr1 + arr2)
print(arr1 * 2)
print(arr2 / 10)

# Useful stats
print(np.mean(arr1))
print(np.max(arr2))
print(np.min(arr1))
print(np.sum(arr1))
>>>>>>> 2bc073d92990917a456f9e8034dd73cce3eae219
