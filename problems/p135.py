r"""
[easy][apple]

Given a binary tree, find a minimum path sum from root to a leaf.
For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
   10
 /    \
5      5
 \      \
  2      1
        /
      -1
"""

import unittest


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def solve(root: Node):
    return 0


class TestClass(unittest.TestCase):
    @staticmethod
    def solve(*args, **kwargs):
        return solve(*args, **kwargs)

    def test_0(self):
        root = Node(
            10,
            left=Node(5, right=Node(2)),
            right=Node(5, right=Node(1, left=Node(-1))),
        )
        result = self.solve(root)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
