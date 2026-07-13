from typing import Optional


class Solution:
    def plusOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_not_nine = None
        current = head
        while current is not None:
            if current.val != 9:
                last_not_nine = current
            current = current.next

        if last_not_nine is None:
            new_head = ListNode(1, head)
            current = head
            while current is not None:
                current.val = 0
                current = current.next
            return new_head

        last_not_nine.val += 1
        current = last_not_nine.next
        while current is not None:
            current.val = 0
            current = current.next
        return head

