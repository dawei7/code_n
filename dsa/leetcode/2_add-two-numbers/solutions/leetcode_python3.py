from typing import Optional


# LeetCode provides ListNode in the judge environment.
class Solution:
    def addTwoNumbers(
        self,
        l1: Optional["ListNode"],
        l2: Optional["ListNode"],
    ) -> Optional["ListNode"]:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            left = l1.val if l1 is not None else 0
            right = l2.val if l2 is not None else 0
            carry, digit = divmod(left + right + carry, 10)
            tail.next = ListNode(digit)
            tail = tail.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummy.next
