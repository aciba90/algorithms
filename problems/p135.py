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
from collections import deque

from ds.trees import BinaryNode as Node


def solve(root: Node):
    # result, cur_sum = float("inf"), 0
    visited, stack = set(), deque((root, ))

    while stack:
        node = stack.pop()
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            stack.append(node)
            node = node.right

    return 0


class TestClass(unittest.TestCase):

    @staticmethod
    def solve(*args, **kwargs):
        return solve(*args, **kwargs)

    def test_0(self):
        root = Node(
            10,
            left=Node(5, right=Node(2)),
            right=Node(5, right=Node(1, left=Node(-1)))
        )
        result = self.solve(root)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
