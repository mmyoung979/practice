# Python imports
import unittest
from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.visited = False

    def add_child(self, node):
        self.children.append(node)


class Graph:
    def __init__(self):
        """
        Create graph
             5 ----> 8 -> 9
             |       |
             v       v
        2 <- 3 -> 4  6 -> 7
             |       |
             v       v
             1 ---> 100
        """
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        node8 = Node(8)
        node9 = Node(9)
        node100 = Node(100)

        node1.add_child(node100)
        node3.add_child(node1)
        node3.add_child(node2)
        node3.add_child(node4)
        node5.add_child(node3)
        node5.add_child(node8)
        node6.add_child(node7)
        node6.add_child(node100)
        node8.add_child(node6)
        node8.add_child(node9)

        self.head = node5

    def dfs(self, node: Node) -> List[int]:
        result = [node.value]
        node.visited = True
        for child in node.children:
            if child.visited:
                continue
            result.extend(self.dfs(child))
        return result

    def bfs(self, node: Node) -> List[int]:
        result = []
        queue = [node]
        while queue:
            current_node = queue.pop(0)
            current_node.visited = True
            result.append(current_node.value)
            for child in current_node.children:
                if child.visited:
                    continue
                child.visited = True
                queue.append(child)

        return result


class Matrix:
    def __init__(self):
        self.matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]

    def skip(self, row: int, col: int) -> bool:
        # Make sure row and col are within bounds
        if row >= self.rows or col >= self.cols or row < 0 or col < 0:
            return True

        # Make sure we don't look at the same location twice
        if self.visited[row][col]:
            return True

        return False

    def dfs(self, row: int, col: int, result=[]) -> List[int]:
        # Make sure row and col are within bounds
        if self.skip(row, col):
            return

        # Record that we have visited this cell
        result.append(self.matrix[row][col])
        self.visited[row][col] = True

        # Up, right, down, left
        self.dfs(row - 1, col, result)
        self.dfs(row, col + 1, result)
        self.dfs(row + 1, col, result)
        self.dfs(row, col - 1, result)

        return result

    def bfs(self, row: int, col: int) -> List[int]:
        result = []
        queue = [(row, col)]
        while queue:
            # Look at first item in queue
            current_cell = queue.pop(0)
            row = current_cell[0]
            col = current_cell[1]

            # Make sure row and col are within bounds
            if self.skip(row, col):
                continue

            # Record that we have visited this cell
            self.visited[row][col] = True
            result.append(self.matrix[row][col])

            # Add up, right, down, left elements to queue
            queue.append((row - 1, col))
            queue.append((row, col + 1))
            queue.append((row + 1, col))
            queue.append((row, col - 1))

        return result


class TestTraversal(unittest.TestCase):
    def test_node_dfs(self):
        graph = Graph()
        assert graph.dfs(graph.head) == [5, 3, 1, 100, 2, 4, 8, 6, 7, 9]

    def test_node_bfs(self):
        graph = Graph()
        assert graph.bfs(graph.head) == [5, 3, 8, 1, 2, 4, 6, 9, 100, 7]

        # Test duplicate filtering
        graph = Graph()
        graph.duplicate_node = Node(11)
        graph.head.add_child(graph.duplicate_node)
        graph.head.add_child(graph.duplicate_node)
        assert graph.bfs(graph.head) == [5, 3, 8, 11, 1, 2, 4, 6, 9, 100, 7]

    def test_matrix_dfs(self):
        matrix = Matrix()
        assert matrix.dfs(0, 0) == [1, 2, 3, 6, 9, 8, 5, 4, 7]

    def test_matrix_bfs(self):
        matrix = Matrix()
        assert matrix.bfs(0, 0) == [1, 2, 4, 3, 5, 7, 6, 8, 9]


if __name__ == "__main__":
    unittest.main()
