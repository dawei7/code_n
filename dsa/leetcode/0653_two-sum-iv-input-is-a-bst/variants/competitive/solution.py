class Solution:
    def findTarget(self, root, k: int) -> bool:
        seen = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if k - node.val in seen:
                return True
            seen.add(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return False
