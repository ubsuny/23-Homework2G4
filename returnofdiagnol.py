def get_diagonal(matrix):
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows != num_cols:
        raise ValueError("Input matrix must be square.")

    diagonal = []

    for i in range(num_rows):
        for j in range(num_cols):
            if i == j:
                diagonal.append(matrix[i][j])

    return diagonal

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal_elements = get_diagonal(matrix)
print(diagonal_elements)  # Output: [1, 5, 9]
