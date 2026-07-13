from typing import Optional


class Solution:
    def connect(self, root: Optional["Node"]) -> Optional["Node"]:
        current_level = root
        while current_level is not None:
            next_head = tail = None
            node = current_level
            while node is not None:
                for child in (node.left, node.right):
                    if child is None:
                        continue
                    if tail is None:
                        next_head = child
                    else:
                        tail.next = child
                    tail = child
                node = node.next
            if tail is not None:
                tail.next = None
            current_level = next_head
        return root
