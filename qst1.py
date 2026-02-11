import numpy as np
arr = np.arange(1, 13)
print("Array:", arr)
print("Data type:", arr.dtype)
print("Shape:", arr.shape)
print("Size:", arr.size)
reshaped_arr = arr.reshape(3, 4)
print("Reshaped Array (3x4):")
print(reshaped_arr)
