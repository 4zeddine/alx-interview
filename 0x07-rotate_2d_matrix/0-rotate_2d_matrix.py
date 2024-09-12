#!/usr/bin/python3
"""Module for rotating a 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix in place"""
    if type(matrix) != list or len(matrix) <= 0:
        return
    containslist = all(map(lambda x: type(x) == list, matrix))
    if not containslist:
        return
    rows = len(matrix)
    cols = len(matrix[0])
    colslists = all(map(lambda x: len(x) == cols, matrix))
    if not colslists:
        return
    col, row = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if row == -1:
            row = rows - 1
            col += 1
        matrix[-1].append(matrix[row][col])
        if col == cols - 1 and row >= -1:
            matrix.pop(row)
        row -= 1
