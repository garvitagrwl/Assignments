import numpy as np

arr3d = np.random.rand(2, 3, 4)
# Move axes: let's move axis 0 to position 2
new_arr = np.moveaxis(arr3d, 0, 2)

print("Q2 Shape before:", arr3d.shape)
print("Q2 Shape after:", new_arr.shape)
