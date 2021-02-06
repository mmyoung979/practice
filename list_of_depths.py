"""List of Depths

Given a binary tree, design an algorithm which creates a linked list of
all the nodes at each depth.

e.g. if you have a tree with Depth D, you'll have D linked lists.
"""


class BinaryTreeNode:
    """Node class for binary tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LinkedListNode:
    """Node class for linked list"""
    def __init__(self, value):
        self.value = value
        self.next = None


def bst_to_ll(root):
    """Convert a binary tree to a list of linked lists
    where each linked list represents all the nodes at
    a given depth of the binary tree.

    We will use a bread-first search to traverse each layer
    of the binary tree.

    This function assumes a complete binary tree.

    root: The root node of the binary tree
    """
    queue = [root]
    max_len = 1
    values = []
    result = []
    while len(queue) != 0:
        curr_node = queue.pop(0)
        values.append(curr_node.value)
        if len(values) == max_len:
            result.append(create_ll(values))
            values = []
            max_len *= 2
        if curr_node.left is not None:
            queue.append(curr_node.left)
        if curr_node.right is not None:
            queue.append(curr_node.right)

    # Check if last layer is not full
    if len(values) != 0:
        result.append(create_ll(values))

    return result


def create_ll(values):
    """Create a linked list from an array of values"""
    
    # If empty array is passed
    if len(values) == 0:
        return
    
    # If only one value is passed
    head = LinkedListNode(values[0])
    if len(values) == 1:
        return head
    
    # Append values to linked list
    curr_node = head
    for value in range(1, len(values)):
        next_node = LinkedListNode(values[value])
        curr_node.next = next_node
        curr_node = curr_node.next

    return head


"""
Input:
       1
     /   \
    2     3
   / \   / \
  4   5 6   7

Expected output:
[
    [1 -> None],
    [2 -> 3 -> None],
    [4 -> 5 -> 6 -> 7 -> None]
]
"""
# Example BST
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

# Check if output is expected
for head in bst_to_ll(root):
    curr_node = head
    while curr_node is not None:
        print(curr_node.value)
        curr_node = curr_node.next
    print('------------')
