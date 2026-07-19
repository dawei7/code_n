from typing import Optional


class Solution:
    def sortLinkedList(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        current = head

        while current.next is not None:
            if current.next.val < 0:
                moved = current.next
                current.next = moved.next
                moved.next = head
                head = moved
            else:
                current = current.next

        return head
