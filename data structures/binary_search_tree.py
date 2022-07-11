# Python imports
import unittest
from typing import List


class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node: Node) -> None:
        if not self.root:
            self.root = node
            return

        current_node = self.root
        while current_node:
            if node.val > current_node.val:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = node
                    return
            else:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = node
                    return

    def remove(self, val: int) -> None:
        if not self.search(val):
            raise ValueError("Node not found")

        current_node = self.root
        parent_node = None
        while current_node:
            if val == current_node.val:
                if not current_node.left and not current_node.right:
                    if parent_node:
                        if val > parent_node.val:
                            parent_node.right = None
                        else:
                            parent_node.left = None
                    else:
                        self.root = None
                    return
                elif current_node.left:
                    if parent_node:
                        parent_node.left = current_node.left
                        self.insert(current_node.right)
                    else:
                        temp_node = current_node.left.right
                        current_node.left.right = current_node.right
                        self.root = current_node.left
                        self.insert(temp_node)
                    return
                else:
                    if parent_node:
                        parent_node.right = current_node.right
                        self.insert(current_node.left)
                    else:
                        temp_node = current_node.right.left
                        current_node.right.left = current_node.left
                        self.root = current_node.right
                        self.insert(temp_node)
                    return
            else:
                parent_node = current_node

            if val > current_node.val:
                current_node = current_node.right
            else:
                current_node = current_node.left

    def search(self, val: int) -> bool:
        if not self.root:
            return False

        current_node = self.root
        while current_node:
            if val == current_node.val:
                return True
            elif val > current_node.val:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return False

    def view(self, in_order: bool = False) -> List[int]:
        if not self.root:
            return []

        if in_order:
            return self.in_order_traversal(self.root)
        return self.pre_order_traversal(self.root)

    def pre_order_traversal(self, node: Node) -> List[int]:
        if not node:
            return []

        return (
            [node.val]
            + self.pre_order_traversal(node.left)
            + self.pre_order_traversal(node.right)
        )

    def in_order_traversal(self, node: Node) -> List[int]:
        if not node:
            return []

        return (
            self.in_order_traversal(node.left)
            + [node.val]
            + self.in_order_traversal(node.right)
        )


class TestBST(unittest.TestCase):
    def create_bst(self) -> BST:
        bst = BST()
        array = [5, 3, 4, 2, 7, 6, 8]
        for num in array:
            bst.insert(Node(num))
        return bst

    def test_insert(self):
        bst = self.create_bst()
        assert bst.root.val == 5
        assert bst.root.left.val == 3
        assert bst.root.left.left.val == 2
        assert bst.root.left.right.val == 4
        assert bst.root.right.val == 7
        assert bst.root.right.left.val == 6
        assert bst.root.right.right.val == 8

    def test_remove(self):
        bst = self.create_bst()
        assert bst.view(in_order=True) == [2, 3, 4, 5, 6, 7, 8]
        bst.remove(2)
        assert bst.view(in_order=True) == [3, 4, 5, 6, 7, 8]
        bst.remove(5)
        assert bst.view(in_order=True) == [3, 4, 6, 7, 8]

        with self.assertRaises(ValueError):
            bst.remove(10)

        bst = BST()
        bst.insert(Node(1))
        bst.remove(1)
        assert bst.root == None
        assert bst.view() == []

    def test_view(self):
        bst = self.create_bst()
        assert bst.view() == [5, 3, 2, 4, 7, 6, 8]
        assert bst.view(in_order=True) == [2, 3, 4, 5, 6, 7, 8]

    def test_search(self):
        bst = self.create_bst()
        for num in range(2, 9):
            assert bst.search(num) == True
        for num in range(9, 100):
            assert bst.search(num) == False


if __name__ == "__main__":
    unittest.main()
