class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head, k: int):
    if head is None or head.next is None:
        return head

    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1

    rotation = k % length
    if rotation == 0:
        return head

    tail.next = head
    new_tail = head
    for _ in range(length - rotation - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head
