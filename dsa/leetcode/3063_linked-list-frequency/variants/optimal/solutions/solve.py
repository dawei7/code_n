class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head: ListNode | None) -> ListNode | None:
    frequencies = {}
    current = head

    while current is not None:
        frequencies[current.val] = frequencies.get(current.val, 0) + 1
        current = current.next

    dummy = ListNode()
    tail = dummy
    for frequency in frequencies.values():
        tail.next = ListNode(frequency)
        tail = tail.next

    return dummy.next
