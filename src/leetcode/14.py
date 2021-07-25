"""
TODO Doc and tests

Time: O(n * m)
Space: O(1)
"""

#
from typing import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        longest_prefix = ""
        min_len = min(map(len, strs))

        for i in range(min_len):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return longest_prefix
            else:
                longest_prefix += char

        return longest_prefix
