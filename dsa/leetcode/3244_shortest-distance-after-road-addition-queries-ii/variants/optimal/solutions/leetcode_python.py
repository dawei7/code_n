from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        next_city = list(range(1, n + 1))
        distance = n - 1
        answer = []

        for source, destination in queries:
            while next_city[source] < destination:
                successor = next_city[source]
                next_city[source] = destination
                source = successor
                distance -= 1
            answer.append(distance)

        return answer
