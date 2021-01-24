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

import unittest
from collections import deque


def get_neighbours(node, n_rows, n_columns):
    neighbours = set()
    i, j = node
    if i > 0:
        neighbours.add((i - 1, j))
    if j > 0:
        neighbours.add((i, j - 1))
    if i < n_rows - 1:
        neighbours.add((i + 1, j))
    if j < n_columns - 1:
        neighbours.add((i, j + 1))
    return neighbours


def is_true(matrix, node):
    return matrix[node[0]][node[1]] == 1


def solve(matrix):
    n_rows, n_columns = len(matrix), len(matrix[0])
    visited = set()
    area = cur_area = 0
    nodes = deque([(0, 0)])

    while nodes:
        node = nodes.popleft()
        if node in visited:
            continue

        visited.add(node)
        if is_true(matrix, node):
            cur_area += 1
        else:
            cur_area = 0

        neighbours = get_neighbours(node, n_rows, n_columns)
        for neighbour in neighbours:
            if is_true(matrix, neighbour):
                nodes.appendleft(neighbour)
            else:
                nodes.append(neighbour)

        area = max(area, cur_area)

    return area


class TestClass(unittest.TestCase):

    @staticmethod
    def solve(*args, **kwargs):
        return solve(*args, **kwargs)

    def test_1(self):
        matrix = [
            [1, 0, 0, 0],
            [1, 0, 1, 1],
            [1, 0, 1, 1],
            [0, 1, 0, 0],
        ]
        result = self.solve(matrix)
        self.assertEqual(result, 4)

    def test_0(self):
        matrix = [[0]]
        result = self.solve(matrix)
        self.assertEqual(result, 0)

    def test_2(self):
        matrix = [[1]]
        result = self.solve(matrix)
        self.assertEqual(result, 1)

    def test_3(self):
        matrix = [
            [1, 0, 0, 0],
            [1, 0, 1, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 0],
        ]
        result = self.solve(matrix)
        self.assertEqual(result, 3)

    def test_4(self):
        matrix = [
            [1, 0, 1, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 0],
            [1, 1, 0, 1],
        ]
        result = self.solve(matrix)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
