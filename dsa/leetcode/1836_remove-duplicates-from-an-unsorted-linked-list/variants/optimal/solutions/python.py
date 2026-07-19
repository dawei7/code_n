"""App-local reference solution for LeetCode 1836."""

from collections import Counter


def solve(head):
    frequencies = Counter()
    current = head
    while current is not None:
        frequencies[current.val] += 1
        current = current.next

    while head is not None and frequencies[head.val] > 1:
        head = head.next

    current = head
    while current is not None and current.next is not None:
        if frequencies[current.next.val] > 1:
            current.next = current.next.next
        else:
            current = current.next

    return head
