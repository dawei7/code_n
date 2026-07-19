from typing import List


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        indegree = [0] * n
        for child in leftChild + rightChild:
            if child == -1:
                continue
            indegree[child] += 1
            if indegree[child] > 1:
                return False

        roots = [node for node, degree in enumerate(indegree) if degree == 0]
        if len(roots) != 1:
            return False

        seen = set()
        stack = roots
        while stack:
            node = stack.pop()
            if node in seen:
                return False
            seen.add(node)
            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    stack.append(child)

        return len(seen) == n
