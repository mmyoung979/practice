class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []


def path_exists(S: Node, E: Node, seen: set = set()) -> bool:
    """
    Determine if a path exists between two
    given nodes in a directed graph

    Args:
        S: Starting node
        E: Ending node
        root: Reference original S value in recursive calls

    Returns:
        True or False depending on whether a path
        exists between the two given nodes or not
    """
    # Mark node as seen to prevent cycles
    seen.add(S)

    # If start and end are the same
    if S == E:
        return True

    # If connection to E found
    if E in S.adjacent:
        return True

    # Search adjacent nodes for connection to E
    for node in S.adjacent:
        if node in seen:
            continue
        if path_exists(node, E, seen):
            return True

    # No connections found
    return False


# Directed graph
"""
1 -> 2 -> 3 -> 1 -> ... (Cycle)

4 -> 5
"""
# Create test nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Build graph connections
node1.adjacent = [node2]
node2.adjacent = [node3]
node3.adjacent = [node1]
node4.adjacent = [node5]

# Test cases and expected outcomes
test_cases = [
    (node1, node1, True),
    (node2, node2, True),
    (node3, node3, True),
    (node4, node4, True),
    (node5, node5, True),
    (node1, node2, True),
    (node1, node3, True),
    (node2, node3, True),
    (node2, node1, True),
    (node3, node1, True),
    (node3, node2, True),
    (node4, node5, True),
    (node1, node4, False),
    (node1, node5, False),
    (node2, node4, False),
    (node2, node5, False),
    (node3, node4, False),
    (node3, node5, False),
    (node4, node1, False),
    (node4, node2, False),
    (node4, node3, False),
    (node5, node1, False),
    (node5, node2, False),
    (node5, node3, False),
    (node5, node4, False),
]

for test_case in test_cases:
    assert path_exists(test_case[0], test_case[1], set()) == test_case[2]
