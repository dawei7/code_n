from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        node_count = len(parents)
        children = [[] for _ in parents]
        for node in range(1, node_count):
            children[parents[node]].append(node)

        order = []
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            stack.extend(children[node])

        subtree_size = [1] * node_count
        highest_score = 0
        highest_count = 0

        for node in reversed(order):
            score = 1
            for child in children[node]:
                subtree_size[node] += subtree_size[child]
                score *= subtree_size[child]

            parent_side = node_count - subtree_size[node]
            if parent_side:
                score *= parent_side

            if score > highest_score:
                highest_score = score
                highest_count = 1
            elif score == highest_score:
                highest_count += 1

        return highest_count
