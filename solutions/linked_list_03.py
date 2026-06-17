"""Solution for linked_list_03: Merge Two Sorted Linked Lists.

Merge two sorted linked lists into a single sorted list.
Two-pointer walk: at each step, attach the smaller head and
advance that head. Append the remaining tail at the end.
Return the merged (values, next) pair. O(n1 + n2) time.
Source: https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/

Inputs passed to solve():
    values1: list of n1 values (sorted ascending).
    next1: list of n1 next-pointers (parallel to values1).
    head1: head of list 1.
    values2: list of n2 values (sorted ascending).
    next2: list of n2 next-pointers (parallel to values2).
    head2: head of list 2.
    n1: length of list 1.
    n2: length of list 2.

Goal:
    (merged_values, merged_next) - the merged sorted list.

Samples:
Sample 1 input:  list1 = [1, 3, 5], list2 = [2, 4, 6]
Sample 1 output: [1, 2, 3, 4, 5, 6]

Sample 2 input:  list1 = [1, 2], list2 = []
Sample 2 output: [1, 2]


"""

def solve(values1, next1, head1, values2, next2, head2, n1, n2):
    # Write your code here.
    return None
