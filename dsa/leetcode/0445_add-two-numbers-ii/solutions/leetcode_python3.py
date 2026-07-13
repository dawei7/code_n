from typing import Optional


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional['ListNode'],
        l2: Optional['ListNode'],
    ) -> Optional['ListNode']:
        first = []
        second = []
        while l1 is not None:
            first.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            second.append(l2.val)
            l2 = l2.next

        head = None
        carry = 0
        while first or second or carry:
            total = carry
            if first:
                total += first.pop()
            if second:
                total += second.pop()
            head = ListNode(total % 10, head)
            carry = total // 10
        return head
