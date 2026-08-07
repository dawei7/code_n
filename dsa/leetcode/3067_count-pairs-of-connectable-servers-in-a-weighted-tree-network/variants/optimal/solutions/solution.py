import sys


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for first, second, weight in edges:
            graph[first].append((second, weight))
            graph[second].append((first, weight))

        sys.setrecursionlimit(max(sys.getrecursionlimit(), 2 * n + 50))

        def count_divisible(node: int, parent: int, distance: int) -> int:
            count = int(distance % signalSpeed == 0)
            for neighbor, weight in graph[node]:
                if neighbor != parent:
                    count += count_divisible(neighbor, node, distance + weight)
            return count

        answer = [0] * n
        for root in range(n):
            qualifying_before = 0
            for neighbor, weight in graph[root]:
                branch_count = count_divisible(neighbor, root, weight)
                answer[root] += qualifying_before * branch_count
                qualifying_before += branch_count

        return answer
