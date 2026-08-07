from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 1
        best_level = 1
        best_sum = float("-inf")

        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if level_sum > best_sum:
                best_sum = level_sum
                best_level = level
            level += 1

        return best_level
