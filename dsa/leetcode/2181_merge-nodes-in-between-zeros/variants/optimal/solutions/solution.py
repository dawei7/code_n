# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head):
        read = head.next
        write = head

        while read:
            segment_sum = 0
            while read.val != 0:
                segment_sum += read.val
                read = read.next

            write.val = segment_sum
            read = read.next
            if read:
                write = write.next
            else:
                write.next = None

        return head
