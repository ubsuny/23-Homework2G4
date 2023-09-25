import numpy as np
import time

def diagonal_elements(matrix):
    """
    Extracts the diagonal elements of a matrix using NumPy and measures the time taken for the operation.

    Parameters:
        matrix (list or numpy.ndarray): The input matrix from which diagonal elements are to be extracted.

    Returns:
        numpy.ndarray: A 1-D NumPy array containing the diagonal elements of the input matrix.
        float: The execution time (in seconds) of the NumPy operation for diagonal element extraction.

    Example:
        >>> matrix = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
        >>> diagonal, numpy_time = diagonal_elements(matrix)
        >>> print("Diagonal elements:", diagonal)
        Diagonal elements: [1 5 9]
        >>> print("NumPy execution time:", numpy_time)
        NumPy execution time: 0.00011110305786132812

    Note:
        This function utilizes NumPy's `np.diag()` function to efficiently extract the diagonal elements
        from the input matrix. The execution time is measured using the time.time() function.
    """
    # Start measuring time for the NumPy operation
    start_time = time.time()

    diagonal = np.diag(matrix)

    # End measuring time for the NumPy operation
    end_time = time.time()
    numpy_execution_time = end_time - start_time

    return diagonal, numpy_execution_time

# Example Unit Test:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

diagonal, numpy_time = diagonal_elements(matrix)
print("Diagonal elements:", diagonal)
print("NumPy execution time:", numpy_time)
