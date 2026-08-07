# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, l = head, 2
        while prev.next:
            curr, cnt = prev, 0
            for _ in range(l):
                if not curr.next:
                    break
                cnt += 1
                curr = curr.next
            l += 1
            if cnt%2:
                prev = curr
                continue
            curr, last = prev.next, None
            for _ in range(cnt):
                curr.next, curr, last = last, curr.next, curr
            prev.next.next, prev.next, prev = curr, last, prev.next
        return head
