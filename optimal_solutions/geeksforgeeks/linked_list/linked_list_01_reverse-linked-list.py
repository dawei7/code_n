"""Optimal solution for linked_list_01: Reverse Linked List.

Iterative in-place reversal. Walk the list with prev, cur,
nxt pointers; on each step, flip cur.next to prev, then
advance. O(n) time, O(1) space. Return the new parallel
``(values, next)`` representation.
"""


def solve(values, next, head, n):
    if n == 0 or head == -1:
        return values, next, -1
    new_next = list(next)
    prev = -1
    cur = head
    new_head = -1
    while cur != -1:
        nxt_node = new_next[cur]
        new_next[cur] = prev
        new_head = cur
        prev = cur
        cur = nxt_node
    return list(values), new_next, new_head
