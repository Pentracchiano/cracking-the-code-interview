# 7 - Given an image represented by an NxN matrix, where each pixel in the image is represented by an integer,
# write a method to rotate the image by 90 degrees. Can you do this in place?
import typing
import pytest


def rotate_matrix(matrix):
    # Assumption: matrix is a list of N lists containing each N integers representing the matrix
    size = len(matrix[0])
    if size <= 1:
        return

    current_size = size
    starting_i, starting_j = 0, 0
    while current_size >= 1:

        first_array_start = starting_i, starting_j
        second_array_start = starting_i, starting_j + current_size - 1
        third_array_start = starting_i + current_size - 1, starting_j + current_size - 1
        fourth_array_start = starting_i + current_size - 1, starting_j

        for i in range(current_size - 1):
            temp = matrix[first_array_start[0]][first_array_start[1] + i]
            matrix[first_array_start[0]][first_array_start[1] + i] = matrix[fourth_array_start[0] - i][fourth_array_start[1]]
            matrix[fourth_array_start[0] - i][fourth_array_start[1]] = matrix[third_array_start[0]][third_array_start[1] - i]
            matrix[third_array_start[0]][third_array_start[1] - i] = matrix[second_array_start[0] + i][second_array_start[1]]
            matrix[second_array_start[0] + i][second_array_start[1]] = temp

        current_size -= 2
        starting_i += 1
        starting_j += 1


def test_rotate_matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotated = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    rotate_matrix(matrix)

    print()
    print(*matrix, sep='\n')
    print()
    print(*rotated, sep='\n')

    assert matrix == rotated

    matrix = [[1, 2, 3, 4, 'a'], [5, 6, 7, 8, 'b'], [9, 10, 11, 12, 'c'], [13, 14, 15, 16, 'd'], ['e', 'f', 'g', 'h', 'i']]
    rotate_matrix(matrix)

    print(*matrix, sep='\n')
