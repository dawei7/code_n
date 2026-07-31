class ListNode:
    """Local equivalent of the singly linked-list node supplied by LeetCode."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next
