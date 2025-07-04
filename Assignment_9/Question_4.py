import numpy as np


two_d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print("Q4: Practice Operations on Array:\n", two_d)


print("\nQ4.1: Max value:", np.max(two_d))


print("Q4.2: Min value:", np.min(two_d))

rows, cols = two_d.shape
print(f"Q4.3: Number of rows = {rows}, Number of columns = {cols}")


print("Q4.4: All elements:")
for row in two_d:
    for val in row:
        print(val, end=' ')
print("\nQ4.4: Specific element at [1][2]:", two_d[1, 2])


total = 0
for row in two_d:
    for val in row:
        total += val
print("Q4.5: Sum using loop:", total)


arr1 = np.array([[1, 2],
                 [3, 4]])
arr2 = np.array([[10, 20],
                 [30, 40]])

print("\nQ4.6: Arithmetic Operations:")
print("Addition:\n", arr1 + arr2)
print("Subtraction:\n", arr2 - arr1)
print("Multiplication:\n", arr1 * arr2)
print("Division:\n", arr2 / arr1)
