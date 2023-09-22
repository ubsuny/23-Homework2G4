# Trial Documentation of Return of Matrix
I have done python coding and now I am writing documentation for this as a practice.

```python
def get_diagonal(matrix):
    """
    Returns the diagonal elements of a square matrix.

    Args:
        matrix (list of lists): The input square matrix.

    Returns:
        list: A list containing the diagonal elements.

    Raises:
        ValueError: If the input matrix is not square (number of rows != number of columns).

    Example:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        diagonal_elements = get_diagonal(matrix)
        # Output: [1, 5, 9]
    """
```

Function Description:

get_diagonal is a function that calculates and returns the diagonal elements of a square matrix.
Arguments:

matrix (list of lists): This argument is the input square matrix for which you want to retrieve the diagonal elements. It should be a list of lists where the number of rows equals the number of columns.
Returns:

list: The function returns a list containing the diagonal elements of the input square matrix.
Raises:

ValueError: If the input matrix is not square (meaning the number of rows is not equal to the number of columns), the function raises a ValueError to indicate that it cannot calculate the diagonal.
Example:

The example provided demonstrates how to use the get_diagonal function:
matrix is defined as a 3x3 square matrix.
The function get_diagonal(matrix) is called to retrieve the diagonal elements.
The result is [1, 5, 9], which are the diagonal elements of the input matrix.
This documentation clarifies the purpose of the function, its input requirements, the expected output, and how it handles potential errors. Users can refer to this documentation to understand how to use the function effectively.