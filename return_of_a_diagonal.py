import numpy as np

# Define your matrix (2D array)
matrix = np.array([[1, 2, 3],
                   [3, 4, 5],
                   [5, 6, 7]])

# Extract the diagonal using Einstein notation
diagonal = np.einsum('ii->i', matrix)

# Print the diagonal elements
print(diagonal)  
