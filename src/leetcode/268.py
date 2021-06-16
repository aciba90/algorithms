"""
268. Missing Number
Easy

Given an array nums containing n distinct numbers in the range [0, n], return the only
number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and
O(n) runtime complexity?
"""

from typing import List
import pytest


def missing_number_0(nums: List[int]) -> int:
    """
    Sorting solution.

    The idea is to sort the arr and iterate looking for the missing number.

    Time: O(nlogn)  (Complexity of sorting)
    Space: O(1)     (Complexity of sorting)
    """
    nums.sort()
    if nums[0] != 0:
        return 0
    for i in range(len(nums) - 1):
        next_num = nums[i + 1] - 1
        if nums[i] != next_num:
            return next_num
    return len(nums)


def missing_number(nums: List[int]) -> int:
    """
    Solution using math.

    Sum of n number = n(n+1)/2

    Time: O(n)
    Space: O(1)
    """
    return (len(nums) * (len(nums) + 1) // 2) - sum(nums)


@pytest.mark.parametrize(
    ["arr", "result"],
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
    ],
)
@pytest.mark.parametrize("fun", [missing_number_0, missing_number])
def test_missing_number(arr, result, fun):
    assert fun(arr) == result
