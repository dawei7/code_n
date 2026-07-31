from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [False] * len(edges)
        answer = -1
        for start in range(len(edges)):
            if visited[start]:
                continue
            first_step = {}
            node = start
            step = 0
            while node != -1 and not visited[node]:
                visited[node] = True
                first_step[node] = step
                step += 1
                node = edges[node]
            if node in first_step:
                answer = max(answer, step - first_step[node])
        return answer
