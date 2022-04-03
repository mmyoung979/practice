# Python imports
import unittest
from typing import List


def binary_search(array: List[int], target: int) -> bool:
    """
    Binary search algorithm

    Args:
        array: Sorted array of integers to search through
        target: Number to search for within array

    Returns:
        Whether or not the target number exists within
        the input array
    """
    start = 0
    end = len(array)
    mid = len(array) // 2
    while start <= end and mid < len(array):
        if target == array[mid]:
            # We have identifed the target number
            return True

        if target > array[mid]:
            # Number is higher than where we checked
            start = mid + 1
        else:
            # Number is lower than where we checked
            end = mid - 1

        # Search in new location
        mid = start + (end - start) // 2

    return False


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        # Create sorted array for testing
        limit = 1000
        array = [num for num in range(0, limit, 2)]

        # Test arbitrary numbers within array
        assert binary_search(array, 74) == True
        assert binary_search(array, 75) == False

        # Test boundaries of array
        assert binary_search(array, 0) == True
        assert binary_search(array, limit) == False
        assert binary_search(array, limit - 2) == True


if __name__ == "__main__":
    # Run tests
    unittest.main()
