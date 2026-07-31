from typing import List, Optional


class Solution:
    def splitCircularLinkedList(
        self, list: Optional[ListNode]
    ) -> List[Optional[ListNode]]:
        slow = list
        fast = list

        while fast.next != list and fast.next.next != list:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        if fast.next.next == list:
            fast = fast.next

        slow.next = list
        fast.next = second_head
        return [list, second_head]
