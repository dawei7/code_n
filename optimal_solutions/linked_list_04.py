"""Optimal solution for linked_list_04: Find Middle of Linked List.

Slow and fast pointers: slow moves 1 step, fast moves 2. When
fast hits the end, slow is at the middle. Return (new_values,
new_next, new_head) with the list unchanged structurally
(only the head is set to the middle index).
"""


def solve(values, next, head, n):
    if n == 0 or head == -1:
        return list(values), list(next), -1
    slow = head
    fast = head
    while fast != -1 and next[fast] != -1:
        slow = next[slow]
        fast = next[next[fast]]
    return list(values), list(next), slow
