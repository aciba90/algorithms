"""
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to
the top?

    1    2    3
"""

import pytest
from functools import lru_cache


@lru_cache(maxsize=None)
def climb_stairs_recursive(n: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return climb_stairs_recursive(n - 2) + climb_stairs_recursive(n - 1)


def climb_stairs(n: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


@pytest.mark.parametrize(
    ["n", "result"],
    [
        (2, 2),
        (3, 3),
    ],
)
@pytest.mark.parametrize(
    "fun",
    [climb_stairs_recursive, climb_stairs],
)
def test_climb_stairs(n, result, fun):
    """
    Example 1:

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Example 2:

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    """
    assert climb_stairs(n) == result
