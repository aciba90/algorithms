"""
[medium][google]

Given an N by M matrix consisting only of 1's and 0's, find the largest
rectangle containing only 1's and returns its area.

For example, given the following matrix:
[
    [1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
]
Return 4.
"""

import pytest


def max_histogram_area(hist):
    """
    Calculates the maximum area of an histogram.

    Naive solution Time: O(n2), Space O(1)
    """
    max_area = 0
    for i in range(len(hist)):
        for j in range(i, len(hist)):
            cur_area = min(hist[i : j + 1]) * (j - i + 1)
            max_area = max(max_area, cur_area)
    return max_area


def solve(matrix):
    """
    TODO
    """
    array = matrix[0]
    max_area = max_histogram_area(array)

    for i in range(1, len(matrix)):
        for j in range(len(array)):
            row = matrix[i]
            if row[j] == 0:
                array[j] = 0
            else:
                array[j] += 1
        max_area = max(max_area, max_histogram_area(array))

    return max_area


def test_max_histogram_area_0():
    assert max_histogram_area([1]) == 1
    assert max_histogram_area([1, 2, 1, 2, 2, 1]) == 6
    assert max_histogram_area([1, 2, 2, 3, 2, 1]) == 8


@pytest.mark.parametrize(
    ["matrix", "result"],
    [
        (
            [
                [1, 0, 0, 0],
                [1, 0, 1, 1],
                [1, 0, 1, 1],
                [0, 1, 0, 0],
            ],
            4,
        ),
        ([[0]], 0),
        ([[1]], 1),
        (
            [
                [1, 0, 0, 0],
                [1, 0, 1, 1],
                [1, 0, 1, 0],
                [0, 1, 0, 0],
            ],
            3,
        ),
        (
            [
                [1, 0, 1, 0],
                [0, 1, 1, 1],
                [0, 0, 1, 0],
                [1, 1, 0, 1],
            ],
            3,
        ),
    ],
)
def test_solution(matrix, result):
    assert solve(matrix) == result
