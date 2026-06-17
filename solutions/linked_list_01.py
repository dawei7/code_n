"""Solution for linked_list_01: Reverse Linked List.

Reverse a singly linked list in place. The list is given as
parallel ``values`` and ``next`` arrays (``next[i] = j`` means
node i's next pointer is j; ``-1`` is null). Return
(new_values, new_next, new_head) - the new pointers and
the index of the new head (the original tail).
Requirement: O(n) time, O(1) extra space.
Source: https://www.geeksforgeeks.org/reverse-a-linked-list/

Inputs passed to solve():
    values: list of n values.
    next: list of n next-pointers (parallel to values).
    head: head node index (always 0 in the setup).
    n: length of the list.

Goal:
    (new_values, new_next, new_head) such that the list is reversed.

Samples:
Sample 1 input:  values = [1, 2, 3, 4], next = [1, 2, 3, -1], head = 0, n = 4
Sample 1 output: (values, next=[-1,0,1,2], new_head=3)

Sample 2 input:  values = [7], next = [-1], head = 0, n = 1
Sample 2 output: (values, next=[-1], new_head=0)


"""

def solve(values, next, head, n):
    # Write your code here.
    return None
