# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        value = 0
        current = head
        while current is not None:
            value = value * 2 + current.val
            current = current.next
        return value
