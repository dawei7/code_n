"""Optimal app-local solution for LeetCode 1019."""


class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next

    answer = [0] * len(values)
    stack = []
    for index, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            answer[stack.pop()] = value
        stack.append(index)

    return answer
