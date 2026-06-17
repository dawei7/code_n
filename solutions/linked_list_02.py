"""Solution for linked_list_02: Detect Cycle in Linked List.

Return True iff the linked list has a cycle. Floyd's tortoise
and hare: walk with slow (1 step) and fast (2 steps); they
meet iff there's a cycle. The setup generates roughly half
the lists with cycles.
Source: https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/

Inputs passed to solve():
    next: list of n next-pointers.
    head: head node index.
    n: length of the list.

Goal:
    True iff the list contains a cycle.

Samples:
Sample 1 input:  next = [1, 2, -1, 0], head = 0, n = 3
Sample 1 output: True (1->2->0)

Sample 2 input:  next = [1, 2, 3, -1], head = 0, n = 4
Sample 2 output: False


"""

def solve(next, head, n):
    # Write your code here.
    return None
