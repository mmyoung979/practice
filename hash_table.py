# Python imports
from math import log
from typing import Any
import unittest


class HashTable:
    def __init__(self, length: int = 4) -> None:
        self.array = [None] * length

        # Total number of items
        self.length = 0

    def __str__(self):
        return repr(self.array)

    def __len__(self):
        return self.length

    def __iter__(self):
        return iter(self.array)

    def hash(self, key) -> int:
        """Get array index for key"""
        return hash(key) % len(self.array)

    def __setitem__(self, key, value) -> None:
        hashed_key = self.hash(key)
        if not self.array[hashed_key]:
            self.array[hashed_key] = [[key, value]]
            self.length += 1
        else:
            for mapping in self.array[hashed_key]:
                if key == mapping[0]:
                    mapping[1] = value
                    return
            self.array[hashed_key].append([key, value])
            self.length += 1

        # Re-hash keys if running out of room in array
        self.adjust()

    def adjust(self) -> None:
        """
        If array needs to be expanded, do so and re-hash
        keys as needed
        """
        if self.length > len(self.array) // 2:
            # Create temporary array to re-hash keys
            temp_hash_table = HashTable(length=len(self.array) * 2)
            temp_array = temp_hash_table.array
            for mapping in self.array:
                if not mapping:
                    # Ignore empty values
                    continue

                # Re-hash keys into temporary array
                for key, value in mapping:
                    hashed_key = temp_hash_table.hash(key)
                    if not temp_array[hashed_key]:
                        temp_array[hashed_key] = [[key, value]]
                    else:
                        temp_array[hashed_key].append([key, value])

            # Replace object array with re-hashed array
            self.array = temp_array

    def __getitem__(self, key) -> Any:
        """Retrieve value for given key"""
        hashed_key = self.hash(key)

        # Check if searched key exists
        if not self.array[hashed_key]:
            self.raise_key_error(key)

        # Multiple [key, value] pairs at hashed index
        if len(self.array[hashed_key]) > 1:
            for mapped_key, value in self.array[hashed_key]:
                if mapped_key == key:
                    return value

            # Hashed index held a key, but not the one that
            # we were looking for, so it doesn't exist
            self.raise_key_error(key)

        # Only one [key, value] pair at hashed index
        return self.array[hashed_key][0][1]

    def update(self, hash_table) -> None:
        for mappings in hash_table:
            if not mappings:
                continue
            for key, value in mappings:
                self.__setitem__(key, value)

    def raise_key_error(self, key):
        """Generic KeyError for HashTable class"""
        raise KeyError(f"Key {key} not found.")


class TestHashTable(unittest.TestCase):
    def test_add_adjust_get(self):
        # HashTable object to test
        hash_table = HashTable()

        # Number of elements to create
        start = 1
        end = 100

        assert len(hash_table.array) == 4

        # Initial [key, value] pairs
        for x in range(start, end):
            hash_table[f"key{x}"] = "value0"

        for x in range(start, end):
            assert hash_table[f"key{x}"] == "value0"

        # Total available slots should have increased
        assert len(hash_table.array) == self.get_adjust_len(end - start)

        # Update [key, value] pairs
        for x in range(start, end):
            hash_table[f"key{x}"] = f"value{x}"

        for x in range(start, end):
            assert hash_table[f"key{x}"] == f"value{x}"

        # Integers for key and value
        hash_table[1] = 2
        assert hash_table[1] == 2

    def get_adjust_len(self, n: int) -> int:
        """Calculate how long HashTable array should be

        Args:
            n: How many [key, value] pairs exist

        Returns:
            Expected length of HashTable array
        """
        return 4 * 2 ** int(log(n, 2))

    def test_update(self):
        # HashTable object to test
        hash_table = HashTable()
        hash_table["key1"] = "value1"
        hash_table["key2"] = "value2"
        hash_table["key3"] = "value3"

        # Second HashTable object to update the first
        hash_table2 = HashTable()
        hash_table2["key3"] = "value0"
        hash_table2["key4"] = "value4"
        hash_table2["key5"] = "value5"

        hash_table.update(hash_table2)

        assert hash_table["key1"] == "value1"
        assert hash_table["key2"] == "value2"
        assert hash_table["key3"] == "value0"
        assert hash_table["key4"] == "value4"
        assert hash_table["key5"] == "value5"
        assert len(hash_table.array) == self.get_adjust_len(5)


if __name__ == "__main__":
    unittest.main()
