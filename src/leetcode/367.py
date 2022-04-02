"""TODO doc, test
optimizable with binary search
"""

class Solution:

    perfect_squares = {1, }
    next_integer = 2

    def isPerfectSquare(self, num: int) -> bool:
        if num in self.perfect_squares:
            return True
        while True:
            next_square = self.next_integer ** 2
            self.next_integer += 1
            self.perfect_squares.add(next_square)
            if next_square == num:
                return True
            if next_square > num:
                return False
