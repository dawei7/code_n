from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0] * len(edges)
        for source, target in enumerate(edges):
            scores[target] += source

        answer = 0
        for node in range(1, len(edges)):
            if scores[node] > scores[answer]:
                answer = node
        return answer
