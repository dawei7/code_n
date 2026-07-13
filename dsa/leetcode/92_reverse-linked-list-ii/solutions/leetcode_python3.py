from typing import Optional


class Solution:
    def reverseBetween(
        self,
        head: Optional["ListNode"],
        left: int,
        right: int,
    ) -> Optional["ListNode"]:
        before = None
        current = head
        for _ in range(1, left):
            before = current
            current = current.next

        segment_tail = current
        previous = None
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        segment_tail.next = current
        if before is None:
            return previous
        before.next = previous
        return head
