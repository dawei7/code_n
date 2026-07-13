from typing import Optional


class Solution:
    def copyRandomList(self, head: Optional["Node"]) -> Optional["Node"]:
        current = head
        while current is not None:
            copy = Node(current.val, current.next)
            current.next = copy
            current = copy.next

        current = head
        while current is not None:
            copy = current.next
            copy.random = current.random.next if current.random is not None else None
            current = copy.next

        dummy = Node(0)
        copy_tail = dummy
        current = head
        while current is not None:
            copy = current.next
            current.next = copy.next
            copy_tail.next = copy
            copy_tail = copy
            current = current.next
        return dummy.next
