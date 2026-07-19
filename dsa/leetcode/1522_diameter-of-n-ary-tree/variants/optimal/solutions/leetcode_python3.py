"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def diameter(self, root: "Node") -> int:
        order = []
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node)
            stack.extend(node.children)

        height = {}
        answer = 0
        for node in reversed(order):
            longest = second = 0
            for child in node.children:
                candidate = height[child] + 1
                if candidate > longest:
                    longest, second = candidate, longest
                elif candidate > second:
                    second = candidate
            answer = max(answer, longest + second)
            height[node] = longest

        return answer
