"""Solution for linked_list_04: Find Middle of Linked List.

Return the index of the middle node of a singly linked
list. Slow and fast pointers: slow moves 1 step, fast
moves 2. When fast hits the end, slow is at the middle.
For even length, the middle is the (n/2)-th node.
Source: https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/

Inputs passed to solve():
    values: list of n values.
    next: list of n next-pointers (parallel to values).
    head: head node index (always 0 in the setup).
    n: length of the list.

Goal:
    (new_values, new_next, mid_index) - the middle index.

Samples:
Sample 1 input:  values = [1, 2, 3, 4, 5], next = [1, 2, 3, 4, -1], head = 0, n = 5
Sample 1 output: mid = 2 (value 3)

Sample 2 input:  values = [1, 2, 3, 4], next = [1, 2, 3, -1], head = 0, n = 4
Sample 2 output: mid = 2 (value 3, the second half's first)


"""

def solve(values, next, head, n):
    # Write your code here.
    return None
