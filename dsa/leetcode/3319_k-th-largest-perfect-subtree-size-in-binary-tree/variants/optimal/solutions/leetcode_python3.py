from typing import Optional


class Solution:
    def kthLargestPerfectSubtree(
        self, root: Optional[TreeNode], k: int
    ) -> int:
        heights = {}
        sizes = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
                continue

            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)
            if left_height >= 0 and left_height == right_height:
                height = left_height + 1
                heights[node] = height
                sizes.append((1 << height) - 1)
            else:
                heights[node] = -1

        sizes.sort(reverse=True)
        return sizes[k - 1] if k <= len(sizes) else -1
