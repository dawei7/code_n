from typing import List


class Solution:
    def distanceK(
        self, root: "TreeNode", target: "TreeNode", k: int
    ) -> List[int]:
        parents = {root: None}
        stack = [root]

        while stack:
            node = stack.pop()
            for child in (node.left, node.right):
                if child is not None:
                    parents[child] = node
                    stack.append(child)

        frontier = [target]
        visited = {target}

        for _ in range(k):
            next_frontier = []
            for node in frontier:
                for neighbor in (node.left, node.right, parents[node]):
                    if neighbor is not None and neighbor not in visited:
                        visited.add(neighbor)
                        next_frontier.append(neighbor)
            frontier = next_frontier
            if not frontier:
                break

        return [node.val for node in frontier]
