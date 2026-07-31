class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head, k: int):
    length = 0
    node = head
    while node is not None:
        length += 1
        node = node.next

    base, extra = divmod(length, k)
    parts = []
    current = head

    for index in range(k):
        parts.append(current)
        part_size = base + (index < extra)

        for _ in range(part_size - 1):
            current = current.next

        if current is not None:
            following = current.next
            current.next = None
            current = following

    return parts
