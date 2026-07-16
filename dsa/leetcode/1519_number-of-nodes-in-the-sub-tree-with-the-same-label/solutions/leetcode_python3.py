from typing import List


class Solution:
    def countSubTrees(
        self, n: int, edges: List[List[int]], labels: str
    ) -> List[int]:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        seen = [0] * 26
        before = [0] * n
        answer = [0] * n
        stack = [(0, -1, False)]

        while stack:
            node, parent, exiting = stack.pop()
            label = ord(labels[node]) - ord("a")
            if exiting:
                answer[node] = seen[label] - before[node]
                continue

            before[node] = seen[label]
            seen[label] += 1
            stack.append((node, parent, True))
            for neighbor in graph[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, False))

        return answer
