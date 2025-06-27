import numpy as np

# Random values
d = np.random.rand(3, 3)
print("Random array:\n", d)

# (4x2) empty array
d = np.empty((4, 2))
print("\n4x2 Empty array:\n", d)

# (4x2) full array
d = np.full((4, 2), 7)
print("\n4x2 Full array (filled with 7):\n", d)

# (3x5) array filled with zeros
d = np.zeros((3, 5))
print("\n3x5 Array filled with zeros:\n", d)

# (4x3x2) array filled with ones
d = np.ones((4, 3, 2))
print("\n4x3x2 Array filled with ones:\n", d)
