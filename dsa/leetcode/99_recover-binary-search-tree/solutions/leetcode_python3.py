from typing import Optional


class Solution:
    def recoverTree(self, root: Optional["TreeNode"]) -> None:
        first = second = previous = None
        current = root

        while current is not None:
            if current.left is None:
                if previous is not None and previous.val > current.val:
                    if first is None:
                        first = previous
                    second = current
                previous = current
                current = current.right
                continue

            predecessor = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                if previous is not None and previous.val > current.val:
                    if first is None:
                        first = previous
                    second = current
                previous = current
                current = current.right

        if first is not None and second is not None:
            first.val, second.val = second.val, first.val
