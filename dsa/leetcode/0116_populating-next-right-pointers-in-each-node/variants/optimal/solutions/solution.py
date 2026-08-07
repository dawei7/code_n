from typing import Optional


class Solution:
    def connect(self, root: Optional["Node"]) -> Optional["Node"]:
        leftmost = root
        while leftmost is not None and leftmost.left is not None:
            node = leftmost
            while node is not None:
                node.left.next = node.right
                node.right.next = node.next.left if node.next is not None else None
                node = node.next
            leftmost = leftmost.left
        return root
