from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        pairs = 0
        histograms = {}
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue

            if node.left is None and node.right is None:
                histogram = [0] * (distance + 1)
                histogram[0] = 1
                histograms[node] = histogram
                continue

            left = histograms.pop(node.left, None)
            right = histograms.pop(node.right, None)
            if left is not None and right is not None:
                for left_distance, left_count in enumerate(left):
                    if left_count == 0:
                        continue
                    for right_distance, right_count in enumerate(right):
                        if left_distance + right_distance + 2 <= distance:
                            pairs += left_count * right_count

            histogram = [0] * (distance + 1)
            for child_histogram in (left, right):
                if child_histogram is None:
                    continue
                for child_distance in range(distance):
                    histogram[child_distance + 1] += child_histogram[child_distance]
            histograms[node] = histogram

        return pairs
