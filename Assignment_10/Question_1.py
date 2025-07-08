import numpy as np

arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])


arr = np.nan_to_num(arr, nan=0)


arr = arr.T

print("Q1 Result:\n", arr)
