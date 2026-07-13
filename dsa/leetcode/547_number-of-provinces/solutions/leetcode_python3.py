from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_count = len(isConnected)
        visited = [False] * city_count
        provinces = 0

        for start in range(city_count):
            if visited[start]:
                continue

            provinces += 1
            visited[start] = True
            stack = [start]

            while stack:
                city = stack.pop()
                for neighbor, connected in enumerate(isConnected[city]):
                    if connected and not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

        return provinces

