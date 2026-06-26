"""Optimal solution for linked_list_02: Detect Cycle.

Floyd's tortoise and hare: walk with slow and fast pointers
that advance 1 and 2 steps at a time respectively. If they
ever meet, there's a cycle; if fast reaches the end, there
isn't. O(n) time, O(1) space.
"""


def solve(next, head, n):
    if n == 0 or head == -1:
        return False
    slow = head
    fast = head
    while fast != -1 and next[fast] != -1:
        slow = next[slow]
        fast = next[next[fast]]
        if slow == fast:
            return True
    return False
