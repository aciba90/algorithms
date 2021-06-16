"""
Given an array of integers, write a function to move all 0's to the end while
mantaining the relative order of the other elements
"""


def move_zeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    for i in range(len(arr) - j):
        arr[len(arr) - i - 1] = 0
    return arr


def test_0():
    assert move_zeros([1, 7, 0, 5, 0]) == [1, 7, 5, 0, 0]
