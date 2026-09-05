import numpy as np

class Matrix:
    def __init__(self, data):
        # Convert Python list → NumPy array
        self.data = np.array(data)

    def multiply(self, other):
        # Use NumPy's built‑in matrix multiplication
        result = np.dot(self.data, other.data)
        return Matrix(result)

    def display(self):
        print(self.data)




M1 = Matrix([
    [1, 2, 3, 4, 5],      # 3 × 5 matrix
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])

M2 = Matrix([
    [1, 2],               # 5 × 2 matrix
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
])

print("Matrix M1:")
M1.display()

print("\nMatrix M2:")
M2.display()

print("\nResult of M1 × M2:")
result = M1.multiply(M2)
result.display()
