"""Practice Breadth First Search"""
class Node:
    """Used for building tree structure"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(node, value):
    """Breadth-first search"""    
    current = node
    queue = [current]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.value == value:
            return True
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return False
    

# Build tree
root = Node(7)
root.left = Node(4)
root.right = Node(12)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(10)
root.right.right = Node(14)

"""
     7
   /   \
  4    12
 / \   / \
3   5 10  14
"""

# Check work
assert bfs(root, 7) == True
assert bfs(root, 8) == False
assert bfs(root, 10) == True
assert bfs(root, 14) == True
assert bfs(root, 15) == False
