from collections import Counter
from typing import List


class Solution:
    def countPairs(
        self,
        n: int,
        edges: List[List[int]],
        queries: List[int],
    ) -> List[int]:
        degree = [0] * n
        shared_edges = Counter()

        for first, second in edges:
            first -= 1
            second -= 1
            degree[first] += 1
            degree[second] += 1
            if first > second:
                first, second = second, first
            shared_edges[first, second] += 1

        sorted_degrees = sorted(degree)
        answers = []

        for query in queries:
            count = 0
            left = 0
            right = n - 1

            while left < right:
                if sorted_degrees[left] + sorted_degrees[right] > query:
                    count += right - left
                    right -= 1
                else:
                    left += 1

            for (first, second), multiplicity in shared_edges.items():
                degree_sum = degree[first] + degree[second]
                if degree_sum > query >= degree_sum - multiplicity:
                    count -= 1

            answers.append(count)

        return answers
