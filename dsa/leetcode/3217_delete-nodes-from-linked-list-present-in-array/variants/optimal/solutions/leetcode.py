# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        removed = set(nums)
        dummy = ListNode(0, head)
        previous = dummy
        current = head

        while current:
            if current.val in removed:
                previous.next = current.next
            else:
                previous = current
            current = current.next

        return dummy.next
