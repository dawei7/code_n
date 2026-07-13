from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(
        self,
        root: Optional['TreeNode'],
        subRoot: Optional['TreeNode'],
    ) -> bool:
        def serialize(tree):
            tokens = []
            stack = [tree]

            while stack:
                node = stack.pop()
                if node is None:
                    tokens.append((0, 0))
                    continue
                tokens.append((1, node.val))
                stack.append(node.right)
                stack.append(node.left)

            return tokens

        pattern = serialize(subRoot)
        failure = [0] * len(pattern)

        for index in range(1, len(pattern)):
            matched = failure[index - 1]
            while matched and pattern[index] != pattern[matched]:
                matched = failure[matched - 1]
            if pattern[index] == pattern[matched]:
                matched += 1
            failure[index] = matched

        matched = 0
        for token in serialize(root):
            while matched and token != pattern[matched]:
                matched = failure[matched - 1]
            if token == pattern[matched]:
                matched += 1
                if matched == len(pattern):
                    return True

        return False

