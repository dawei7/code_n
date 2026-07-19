from collections import Counter
from typing import Optional


class Solution:
    def deleteDuplicatesUnsorted(
        self, head: Optional["ListNode"]
    ) -> Optional["ListNode"]:
        frequencies = Counter()
        current = head
        while current is not None:
            frequencies[current.val] += 1
            current = current.next

        dummy = ListNode(0, head)
        current = dummy
        while current.next is not None:
            if frequencies[current.next.val] > 1:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next
