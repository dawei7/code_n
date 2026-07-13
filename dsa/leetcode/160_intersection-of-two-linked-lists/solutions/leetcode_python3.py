from typing import Optional


class Solution:
    def getIntersectionNode(
        self, headA: Optional["ListNode"], headB: Optional["ListNode"]
    ) -> Optional["ListNode"]:
        first = headA
        second = headB
        while first is not second:
            first = headB if first is None else first.next
            second = headA if second is None else second.next
        return first
