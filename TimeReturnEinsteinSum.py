import numpy as np
import time

# Define your matrix (2D array)
matrix = np.array([[1, 2, 3],
                   [3, 4, 5],
                   [5, 6, 7]])

# Measure the execution time
start_time = time.time()

# Extract the diagonal using Einstein notation
diagonal = np.einsum('ii->i', matrix)

# Calculate the execution time
end_time = time.time()
execution_time = end_time - start_time

# Print the diagonal elements and execution time
print("Diagonal:", diagonal)
print("Execution Time:", execution_time, "seconds")

