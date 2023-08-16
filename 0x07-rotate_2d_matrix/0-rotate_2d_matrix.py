#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions
and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2d square matrix 90 degrees
    Args:
        matrix (list): 2d square
    Return:
        None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
