# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val >= 5:
            head = ListNode(0, head)

        current = head
        while current:
            current.val = (current.val * 2) % 10
            if current.next and current.next.val >= 5:
                current.val += 1
            current = current.next

        return head
