import numpy as np
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
addition = A + B
multiplication = np.dot(A, B)
transpose_A = A.T
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Addition:\n", addition)
print("Matrix Multiplication:\n", multiplication)
print("Transpose of A:\n", transpose_A)
