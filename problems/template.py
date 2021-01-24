"""
[easy][company]

<description>
"""

import unittest


def solve():
    pass


class TestClass(unittest.TestCase):

    @staticmethod
    def solve(*args, **kwargs):
        return solve(*args, **kwargs)

    def test_0(self):
        result = self.solve()
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
