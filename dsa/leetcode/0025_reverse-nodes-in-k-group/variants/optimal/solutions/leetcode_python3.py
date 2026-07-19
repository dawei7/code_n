from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional["ListNode"], k: int) -> Optional["ListNode"]:
        sentinel = ListNode(0, head)
        group_prev = sentinel

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return sentinel.next

            group_next = kth.next
            previous = group_next
            current = group_prev.next
            while current is not group_next:
                following = current.next
                current.next = previous
                previous = current
                current = following

            old_start = group_prev.next
            group_prev.next = kth
            group_prev = old_start
