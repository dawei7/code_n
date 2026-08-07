# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        frequencies = {}
        current = head

        while current is not None:
            frequencies[current.val] = frequencies.get(current.val, 0) + 1
            current = current.next

        dummy = ListNode()
        tail = dummy
        for frequency in frequencies.values():
            tail.next = ListNode(frequency)
            tail = tail.next

        return dummy.next
