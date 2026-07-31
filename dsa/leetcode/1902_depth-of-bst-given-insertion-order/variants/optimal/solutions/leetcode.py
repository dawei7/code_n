from typing import List


class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        size = len(order)
        insertion_time = [0] * size
        for time, value in enumerate(order):
            insertion_time[value - 1] = time

        left_child = [-1] * size
        right_child = [-1] * size
        stack: List[int] = []

        for node in range(size):
            last_popped = -1
            while stack and insertion_time[stack[-1]] > insertion_time[node]:
                last_popped = stack.pop()
            if stack:
                right_child[stack[-1]] = node
            if last_popped != -1:
                left_child[node] = last_popped
            stack.append(node)

        maximum_depth = 0
        pending = [(stack[0], 1)]
        while pending:
            node, depth = pending.pop()
            maximum_depth = max(maximum_depth, depth)
            if left_child[node] != -1:
                pending.append((left_child[node], depth + 1))
            if right_child[node] != -1:
                pending.append((right_child[node], depth + 1))
        return maximum_depth
