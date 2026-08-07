from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next

        previous = None
        while slow:
            following = slow.next
            slow.next = previous
            previous = slow
            slow = following

        answer = 0
        first = head
        second = previous
        while second:
            answer = max(answer, first.val + second.val)
            first = first.next
            second = second.next
        return answer
