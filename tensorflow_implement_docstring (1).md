import tensorflow as tf
import time

def diagonal_elements(matrix):
    """
    Extracts the diagonal elements of a matrix using TensorFlow and measures the time taken for the operation.

    Parameters:
        matrix (tf.Tensor or list of lists): The input matrix from which diagonal elements are to be extracted.

    Returns:
        numpy.ndarray: A 1-D NumPy array containing the diagonal elements of the input matrix.
        float: The execution time (in seconds) of the TensorFlow operation for diagonal element extraction.

    Example:
        >>> matrix = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
        >>> diagonal, tensorflow_time = diagonal_elements(matrix)
        >>> print("Diagonal elements:", diagonal)
        Diagonal elements: [1 5 9]
        >>> print("TensorFlow execution time:", tensorflow_time)
        TensorFlow execution time: 0.0013298988342285156

    Note:
        This function uses TensorFlow's tf.linalg.diag_part() function to efficiently extract the diagonal elements
        from the input matrix. The execution time is measured using the time.time() function.

        Ensure that TensorFlow is installed and compatible with your GPU for GPU acceleration to work correctly.
    """
    # Start measuring time for the TensorFlow operation
    start_time = time.time()

    with tf.device('/GPU:0'):
        diagonal = tf.linalg.diag_part(matrix)

    # End measuring time for the TensorFlow operation
    end_time = time.time()
    tensorflow_execution_time = end_time - start_time

    return diagonal.numpy(), tensorflow_execution_time

# Example Unit Test:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

diagonal, tensorflow_time = diagonal_elements(matrix)
print("Diagonal elements:", diagonal)
print("TensorFlow execution time:", tensorflow_time)
