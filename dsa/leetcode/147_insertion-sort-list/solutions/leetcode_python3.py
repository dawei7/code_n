from typing import Optional


class Solution:
    def insertionSortList(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        dummy = ListNode()
        current = head
        while current is not None:
            following = current.next
            position = dummy
            while position.next is not None and position.next.val <= current.val:
                position = position.next
            current.next = position.next
            position.next = current
            current = following
        return dummy.next
