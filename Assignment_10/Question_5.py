import numpy as np
from scipy import stats
#creating numpy 1d array
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])

# average of the arrays

avg = (arr1 + arr2) / 2
print("Average of NumPy arrays:\n", avg)


a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[6, 5, 4], [3, 2, 1]])
combined = np.concatenate((a, b), axis=0)

print("Mean:", np.mean(combined))
print("Median:", np.median(combined))
print("Mode:", stats.mode(combined, axis=None, keepdims=True).mode[0])
