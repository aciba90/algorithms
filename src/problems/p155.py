"""
[#155][medium][mongodb]

Given a list of elements, find the majority element, which appears more than
half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""

import unittest


def solve(array):
    """
    Worst-case complexity: Time O(n), space O(n)
    """
    freq = len(array) // 2.0
    frequencies = dict()
    max_freq = 0
    item = float("nan")
    for number in array:
        if number not in frequencies:
            frequencies[number] = 1
        else:
            frequencies[number] += 1
        max_freq = max(max_freq, frequencies[number])
        if max_freq >= freq:
            item = number
            break
    return item


class TestClass(unittest.TestCase):
    @staticmethod
    def solve(*args, **kwargs):
        return solve(*args, **kwargs)

    def test_0(self):
        result = self.solve([1, 2, 1, 1, 3, 4, 0])
        self.assertEqual(result, 1)

    def test_1(self):
        result = self.solve([1, 2, 2, 2, 1, 2, 3, 2, 4, 0])
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
