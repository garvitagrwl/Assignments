import numpy as np
arr = np.array([[1, 2, np.nan], [4, np.nan, 6]])


col_mean = np.nanmean(arr, axis=0)


inds = np.where(np.isnan(arr))


arr[inds] = np.take(col_mean, inds[1])

print("Q3 Result:\n", arr)
