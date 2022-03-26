# 8 - Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0.
import pytest


def zero_matrix(matrix):
    # Time: O(nm)
    # Memory: O(n+m)


    # I could either use a set putting the indices
    # or a boolean array. It depends on how many columns / indices I would expect to have to be zeroed out. The
    # memory complexity is the same.
    rows = len(matrix)
    columns = len(matrix[0])

    rows_to_zero_out = [False] * rows
    columns_to_zero_out = [False] * columns

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                rows_to_zero_out[i] = True
                columns_to_zero_out[j] = True

    for i in range(rows):
        if rows_to_zero_out[i]:
            zero_row(matrix, i)

    for j in range(columns):
        if columns_to_zero_out[j]:
            zero_column(matrix, j)


def zero_row(matrix, index):
    columns = len(matrix[0])

    for j in range(columns):
        matrix[index][j] = 0


def zero_column(matrix, index):
    rows = len(matrix)

    for i in range(rows):
        matrix[i][index] = 0


def zero_matrix_improved(matrix):
    # This version avoids using other arrays because you already have arrays: the matrix itself is composed of them.
    # Therefore, we use the first row and first column to signal which rows and columns will have to be zeroed out.
    rows = len(matrix)
    columns = len(matrix[0])

    first_row_has_zero = False
    first_column_has_zero = False

    for j in range(columns):
        if matrix[0][j] == 0:
            first_row_has_zero = True

    for i in range(rows):
        if matrix[i][0] == 0:
            first_column_has_zero = True

    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, rows):
        if matrix[i][0] == 0:
            zero_row(matrix, i)

    for j in range(1, columns):
        if matrix[0][j] == 0:
            zero_column(matrix, j)

    if first_row_has_zero:
        zero_row(matrix, 0)

    if first_column_has_zero:
        zero_column(matrix, 0)


def test_zero_matrix():
    matrix = [[1, 0, 3], [4, 1, 6], [7, 8, 9], [1, 7, 3]]

    print()
    print(*matrix, sep='\n')
    print()

    zero_matrix(matrix)

    print(*matrix, sep='\n')


def test_zero_matrix_improved():
    matrix = [[0, 0, 3], [4, 1, 6], [7, 8, 9], [1, 7, 1]]

    print()
    print(*matrix, sep='\n')
    print()

    zero_matrix_improved(matrix)

    print(*matrix, sep='\n')
