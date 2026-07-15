from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        dummy = ListNode(0, head)
        last = {}
        prefix = 0
        current = dummy

        while current is not None:
            prefix += current.val
            last[prefix] = current
            current = current.next

        prefix = 0
        current = dummy
        while current is not None:
            prefix += current.val
            current.next = last[prefix].next
            current = current.next

        return dummy.next
