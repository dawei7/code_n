from typing import Optional


class Solution:
    def detectCycle(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                entry = head
                while entry is not slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None
