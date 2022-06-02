"""
Quick Sort Algorithm

1. Randomize the given input
2. Select a pivot point
3. Find a number to the left that is greater than the pivot
    and a number to the right that is less than the pivot,
    and then switch them
4. Switch the pivot with the greatest number to the right that is less than the pivot if one exists
5. Repeat steps 2-4 recursively with the left and right halves of the array around the pivot
"""

# Python imports
from random import randint
from typing import List
import unittest


def quicksort(array: List[int]) -> None:
    # Randomize the input
    for i in range(len(array)):
        j = randint(0, len(array) - 1)
        array[i], array[j] = array[j], array[i]

    # Sort the array
    _quicksort(array, 0, len(array))


def _quicksort(array: List[int], start: int, end: int) -> None:
    # Recursive base case
    if start >= end - 1:
        return

    # Partition around pivot and return the pivot's final index after partitioning
    pivotIdx = partition(array, start, end)

    # Recursively continue to partition the left and right halves around the pivot
    _quicksort(array, start, pivotIdx)
    _quicksort(array, pivotIdx + 1, end)


def partition(array: List[int], start: int, end: int) -> int:
    # Number to sort other numbers around
    pivot = array[start]

    # Left (i) and right (j) index pointers
    i = start + 1
    j = end - 1

    while i <= j:
        # Stop looking when a number on the left is greater than the pivot
        while i <= j and array[i] <= pivot:
            i += 1

        # Stop looking when a number on the right is less than the pivot
        while i <= j and array[j] > pivot:
            j -= 1

        # Swap the left and right numbers if appropriate and move on
        if i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    # Swap the pivot with the largest number that is less than the pivot
    array[start], array[j] = array[j], array[start]

    # Return the final index of the pivot
    return j


class TestQuickSort(unittest.TestCase):
    def test_quicksort(self):
        # Arbitrary test case
        array = [3, 2, 1]
        quicksort(array)
        assert array == [1, 2, 3]

        # Already sorted
        array = [1, 2, 3]
        quicksort(array)
        assert array == [1, 2, 3]

        # Only one element
        array = [1]
        quicksort(array)
        assert array == [1]

        # Empty array
        array = []
        quicksort(array)
        assert array == []

        # Large amount of input
        size = 10000
        array = [None] * size
        for idx in range(size):
            array[idx] = randint(0, size)

        expected_result = sorted(array)
        quicksort(array)
        assert array == expected_result


if __name__ == "__main__":
    unittest.main()
