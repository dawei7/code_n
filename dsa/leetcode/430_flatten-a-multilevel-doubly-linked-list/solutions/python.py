"""Optimal app-local solution for LeetCode 430."""

from types import SimpleNamespace


def solve(nodes):
    def build(items):
        head = None
        previous = None
        for value, child_items in items:
            node = SimpleNamespace(val=value, prev=previous, next=None, child=None)
            node.child = build(child_items) if child_items else None
            if previous is None:
                head = node
            else:
                previous.next = node
            previous = node
        return head

    head = build(nodes)
    if head is None:
        return None

    stack = [head]
    previous = None
    while stack:
        current = stack.pop()
        if current.next is not None:
            stack.append(current.next)
        if current.child is not None:
            stack.append(current.child)
        if previous is not None:
            previous.next = current
            current.prev = previous
        current.child = None
        previous = current
    return head
