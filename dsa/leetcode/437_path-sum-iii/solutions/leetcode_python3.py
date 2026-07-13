from collections import defaultdict
from typing import Optional


class Solution:
    def pathSum(self, root: Optional['TreeNode'], targetSum: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1

        def count_paths(node: Optional['TreeNode'], current_sum: int) -> int:
            if node is None:
                return 0
            current_sum += node.val
            total = prefix_counts[current_sum - targetSum]
            prefix_counts[current_sum] += 1
            total += count_paths(node.left, current_sum)
            total += count_paths(node.right, current_sum)
            prefix_counts[current_sum] -= 1
            return total

        return count_paths(root, 0)
