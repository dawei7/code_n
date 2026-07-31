from random import choice


class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: ListNode | None):
        self.values = []
        current = head
        while current is not None:
            self.values.append(current.val)
            current = current.next

    def getRandom(self) -> int:
        return choice(self.values)


def solve(head: ListNode | None, draws: int) -> list[int]:
    solution = Solution(head)
    return [solution.getRandom() for _ in range(draws)]
