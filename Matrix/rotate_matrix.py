def rotate_matrix_by_90_degree(matrix):
    row_length = len(matrix)
    column_length = len(matrix[0])

    result = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            result[c][row_length - 1 - r] = matrix[r][c]

    return result

def rotate_matrix_by_minus_90_degree(matrix):
    row_length = len(matrix)
    column_length = len(matrix[0])

    result = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            result[row_length - c][r] = matrix[r][c]

    return result

def rotate_matrix_by_180_degree(matrix):
    row_length = len(matrix)
    column_length = len(matrix[0])

    result = [[0] * column_length for _ in range(row_length)]
    for r in range(row_length):
        for c in range(column_length):
            result[row_length - r - 1][column_length - c - 1] = matrix[r][c]

    return result

a = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]

print(rotate_matrix_by_90_degree(a))
print(rotate_matrix_by_minus_90_degree(a))
print(rotate_matrix_by_180_degree(a))
