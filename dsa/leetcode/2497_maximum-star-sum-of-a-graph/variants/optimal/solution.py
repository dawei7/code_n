import heapq


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        best_neighbors = [[] for _ in vals]

        if k > 0:
            for left, right in edges:
                if vals[right] > 0:
                    heapq.heappush(best_neighbors[left], vals[right])
                    if len(best_neighbors[left]) > k:
                        heapq.heappop(best_neighbors[left])

                if vals[left] > 0:
                    heapq.heappush(best_neighbors[right], vals[left])
                    if len(best_neighbors[right]) > k:
                        heapq.heappop(best_neighbors[right])

        return max(vals[node] + sum(best_neighbors[node]) for node in range(len(vals)))
