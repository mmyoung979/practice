"""Practice Depth First Search"""
class Node:
    """Used for building tree structure"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(node, value):
    """Depth-first search"""
    # Base case
    if value == node.value:
        return True
    
    # Traverse tree to the left
    if node.left is not None:
        if dfs(node.left, value):
            return True
        
    # Traverse tree to the right
    if node.right is not None:
        if dfs(node.right, value):
            return True
        
    # Value not found
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
assert dfs(root, 7) == True
assert dfs(root, 8) == False
assert dfs(root, 10) == True
assert dfs(root, 14) == True
assert dfs(root, 15) == False
