#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Without this line, the changes made to the new one would affect the old one
        using varous methods such as list splicing and the copy method """
    new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2
    return (new_matrix)
