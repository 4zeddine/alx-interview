#!/usr/bin/python3
"""Module got solving Island Perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    per = 0
    if type(grid) is not list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cons in enumerate(row):
            if cons == 0:
                continue
            case = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            per += sum(case)
    return per
