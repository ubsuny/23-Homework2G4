import numpy as np
import time

def extract_diagonal_einsum(matrix):
    """
    Extracts the diagonal elements of a square matrix using NumPy's Einstein notation and measures the execution time.

    Parameters:
        matrix (numpy.ndarray): A square matrix from which diagonal elements are to be extracted.

    Returns:
        numpy.ndarray: A 1-D NumPy array containing the diagonal elements of the input matrix.
        float: The execution time (in seconds) for the diagonal element extraction.

    Example:
        >>> matrix = np.array([[1, 2, 3],
                               [3, 4, 5],
                               [5, 6, 7]])
        >>> diagonal, execution_time = extract_diagonal_einsum(matrix)
        >>> print("Diagonal:", diagonal)
        Diagonal: [1 4 7]
        >>> print("Execution Time:", execution_time, "seconds")
        Execution Time: 8.106231689453125e-06 seconds

    Note:
        This function uses NumPy's np.einsum() function with Einstein notation to efficiently extract the diagonal
        elements from the input square matrix. The execution time is measured using the time.time() function.

    Warning:
        Ensure that the input matrix is square (has the same number of rows and columns) to avoid errors.
    """
    # Measure the execution time
    start_time = time.time()

    # Extract the diagonal using Einstein notation
    diagonal = np.einsum('ii->i', matrix)

    # Calculate the execution time
    end_time = time.time()
    execution_time = end_time - start_time

    return diagonal, execution_time

# Example Unit Test:
matrix = np.array([[1, 2, 3],
                   [3, 4, 5],
                   [5, 6, 7]])

diagonal, execution_time = extract_diagonal_einsum(matrix)
print("Diagonal:", diagonal)
print("Execution Time:", execution_time, "seconds")
