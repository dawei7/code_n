class Solution:
    def levelMedian(self, root: Optional[TreeNode], level: int) -> int:
        current = [root]
        depth = 0

        while current:
            if depth == level:
                return current[len(current) // 2].val

            following = []
            for node in current:
                if node.left is not None:
                    following.append(node.left)
                if node.right is not None:
                    following.append(node.right)

            current = following
            depth += 1

        return -1
