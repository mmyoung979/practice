"""
Input: Two linked lists
Output: If the 2 linked list nodes were combined into integers
        (i.e. 7 -> 1 -> 6 = 617 and 5 -> 9 -> 2 = 295)
        and added together (617 + 912 = 912), the result should
        be a reversed linked list for this sum
        (i.e. 912 = 2 -> 1 -> 9)

Example input: 7 -> 1 -> 6, 5 -> 9 -> 2
Example output: 2 -> 1 -> 9
"""
# Node for singly-linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def sum_lists(l1, l2):
    """Add the reversed integers of two linked lists
    and output the reversed sum in linked list form
    as described in the file's main docstring.
    """
    int_one = linked_list_to_int(l1)
    int_two = linked_list_to_int(l2)
    total = int_one + int_two
    total = list(str(total))
    total.reverse()
    total = [int(x) for x in total]
    head = Node(total[0])
    curr_node = head
    for value in range(1, len(total)):
        curr_node.next = Node(total[value])
        curr_node = curr_node.next
    return head


def append_linked_list_nodes(array, node):
    """Append linked list node values to regular list"""
    curr_node = node
    while curr_node is not None:
        array.append(curr_node.value)
        curr_node = curr_node.next


def linked_list_to_int(linked_list):
    """Get values from linked list, reverse them, and combine into integer"""
    array = []
    append_linked_list_nodes(array, linked_list)
    array.reverse()
    array = [str(x) for x in array]
    return int(''.join(array))


def create_linked_list(array_of_3_ints):
    """Create linked list for testing"""
    node = Node(array_of_3_ints[0])
    node.next = Node(array_of_3_ints[1])
    node.next.next = Node(array_of_3_ints[2])

    return node

# Create inputs for testing
l1 = create_linked_list([7, 1, 6])
l2 = create_linked_list([5, 9, 2])

# Expected results for testing
expected_output = list(str(617 + 295))
expected_output.reverse()
expected_output = [int(x) for x in expected_output]

# Run test
curr_node = sum_lists(l1, l2)
counter = 0
while curr_node is not None:
    try:
        assert curr_node.value == expected_output[counter]
        curr_node = curr_node.next
        counter += 1
    except AssertionError as err:
        print('ASSERTION ERROR\n---------')
        print(f'Counter Value:\t\t{counter}')
        print(f'Expected Result:\t{expected_output[counter]}')
        print(f'Actual Result:\t\t{curr_node.value}')
        print()
        raise err
