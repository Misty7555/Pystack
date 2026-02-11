import numpy as np
arr = np.arange(1, 21)
print("Original Array:")
print(arr)
even_numbers = arr[arr % 2 == 0]
print("\nEven Numbers:")
print(even_numbers)
greater_than_10 = arr[arr > 10]
print("\nNumbers Greater Than 10:")
print(greater_than_10)