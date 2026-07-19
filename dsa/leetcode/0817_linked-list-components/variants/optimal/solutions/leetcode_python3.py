from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        selected = set(nums)
        components = 0
        current = head
        while current is not None:
            if current.val in selected and (
                current.next is None or current.next.val not in selected
            ):
                components += 1
            current = current.next
        return components
