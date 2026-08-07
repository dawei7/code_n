from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        nodes = [root]
        adjacency = [[]]

        for index, node in enumerate(nodes):
            for child in (node.left, node.right):
                if child is None:
                    continue
                child_index = len(nodes)
                nodes.append(child)
                adjacency.append([index])
                adjacency[index].append(child_index)

        answer = nodes[0].val

        for start in range(len(nodes)):
            seen = set()
            stack = [(start, -1, 0, False)]

            while stack:
                node, parent, path_sum, exiting = stack.pop()
                value = nodes[node].val

                if exiting:
                    seen.remove(value)
                    continue

                if value in seen:
                    continue

                path_sum += value
                answer = max(answer, path_sum)
                seen.add(value)
                stack.append((node, parent, path_sum, True))

                for neighbor in adjacency[node]:
                    if neighbor != parent:
                        stack.append((neighbor, node, path_sum, False))

        return answer
