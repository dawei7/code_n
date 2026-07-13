class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        if root is None:
            return []

        traversal = []
        stack = [root]
        while stack:
            node = stack.pop()
            traversal.append(node.val)
            stack.extend(reversed(node.children))

        return traversal

