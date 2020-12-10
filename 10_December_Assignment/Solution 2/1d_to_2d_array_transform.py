import numpy as np

array_1d = np.array([21, 34, 26, 88, 65, 98, 52, 2, 11, 43])

array_2d = np.reshape(array_1d, (2, 5))
print("1D: ", array_1d)
print("2D: ", array_2d)