import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, columns = len(grid), len(grid[0])
        ordered = sorted((threshold, index) for index, threshold in enumerate(queries))
        answer = [0] * len(queries)
        frontier = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        reached = 0

        for threshold, query_index in ordered:
            while frontier and frontier[0][0] < threshold:
                _, row, column = heapq.heappop(frontier)
                reached += 1
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row, next_column = row + dr, column + dc
                    if 0 <= next_row < rows and 0 <= next_column < columns and (next_row, next_column) not in seen:
                        seen.add((next_row, next_column))
                        heapq.heappush(frontier, (grid[next_row][next_column], next_row, next_column))
            answer[query_index] = reached

        return answer
