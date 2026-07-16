from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(
        self,
        head: Optional[ListNode],
        m: int,
        n: int,
    ) -> Optional[ListNode]:
        current = head

        while current is not None:
            for _ in range(1, m):
                if current.next is None:
                    return head
                current = current.next

            after_deleted = current.next
            for _ in range(n):
                if after_deleted is None:
                    break
                after_deleted = after_deleted.next

            current.next = after_deleted
            current = after_deleted

        return head
