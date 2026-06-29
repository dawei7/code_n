


def solve():
    class BSTIterator:
        def __init__(self, root: TreeNode):
            self.stack = []
            self._push_left(root)

        def _push_left(self, node):
            while node:
                self.stack.append(node)
                node = node.left

        def next(self) -> int:
            node = self.stack.pop()
            val = node.val
            if node.right:
                self._push_left(node.right)
            return val

        def hasNext(self) -> bool:
            return len(self.stack) > 0


if __name__ == "__main__":
    solve()
