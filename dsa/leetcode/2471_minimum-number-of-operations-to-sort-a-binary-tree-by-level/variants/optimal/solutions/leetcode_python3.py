from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
TreeNode = object


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        answer = 0
        queue = deque([root])

        while queue:
            values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            order = sorted(range(len(values)), key=values.__getitem__)
            visited = [False] * len(values)
            for start in range(len(values)):
                if visited[start] or order[start] == start:
                    continue

                cycle_length = 0
                index = start
                while not visited[index]:
                    visited[index] = True
                    cycle_length += 1
                    index = order[index]
                answer += cycle_length - 1

        return answer
