"""
Input: Linked list, partition value
Output: Linked list with first half values below partition, second half above partition

Example input: 3 5 8 5 10 2 1 [partition = 5]
Example output: 3 2 1 5 8 5 10
"""
# Node for singly-linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def partition_linked_list(head, partition):
    """Re-order linked list according to partition

    head      -- beginning of the linked list
    partition -- numbers less than this value should be at the
                 beginning of the new linked list
    """
    # Edge case where empty linked list is given as input
    if head is None:
        return None
    
    # Nodes at beginning (left) and end (right) of the resulted linked list
    left_side = []
    right_side = []
    
    # Iterate through nodes, sorting by the partition value
    curr_node = head
    while curr_node is not None:
        if curr_node.value < partition:
            left_side.append(curr_node)
        else:
            right_side.append(curr_node)
        curr_node = curr_node.next
        
    # Create new output linked list from 
    for node in range(len(left_side) - 1):
        left_side[node].next = left_side[node + 1]
    left_side[node + 1].next = right_side[0]
    for node in range(len(right_side) - 1):
        right_side[node].next = right_side[node + 1]
    right_side[node + 1].next = None
    
    # Return head of the resulting linked list
    return left_side[0]


def create_linked_list():
    """Create linked list for testing
    3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
    """
    node = Node(3)
    node.next = Node(5)
    node.next.next = Node(8)
    node.next.next.next = Node(5)
    node.next.next.next.next = Node(10)
    node.next.next.next.next.next = Node(2)
    node.next.next.next.next.next.next = Node(1)
    
    return node


def test_partition_linked_list(partition, expected_output):
    """Assert that partition_linked_list() outputs the same values
    as expected_output for a given partition value.
    """
    head = create_linked_list()
    counter = 0
    curr_node = partition_linked_list(head, partition)
    while curr_node is not None:
        try:
            assert curr_node.value == expected_output[counter]
            curr_node = curr_node.next
            counter += 1
        except AssertionError as err:
            print('ASSERTION ERROR\n---------')
            print(f'Partition Value:\t{partition}')
            print(f'Counter Value:\t\t{counter}')
            print(f'Expected Result:\t{expected_output[counter]}')
            print(f'Actual Result:\t\t{curr_node.value}')
            print()
            raise err

# Test case 1
partition = 5
expected_output = [3, 2, 1, 5, 8, 5, 10]
test_partition_linked_list(partition, expected_output)

# Test case 2
partition = 7
expected_output = [3, 5, 5, 2, 1, 8, 10]
test_partition_linked_list(partition, expected_output)
