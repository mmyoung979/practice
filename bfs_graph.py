"""Practice Breadth First Search"""
def bfs(graph):
    """Breadth-first search"""
    result = []
    current = 'A'
    queue = [current]
    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current)
        for child in graph[current]:
            queue.append(child)
    return result

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G', 'H'],
    'E': [],
    'F': ['I', 'J'],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

"""
        A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I  J    K
"""

# Check work
assert bfs(graph) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
