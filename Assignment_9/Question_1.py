import numpy as np


one_d = np.array([10, 20, 30])


two_d = np.array([[1, 2, 3],
                  [4, 5, 6]])


combined = np.vstack([two_d, one_d.reshape(1, -1)])
print("Q1: Combined Array:\n", combined)
