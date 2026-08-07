from heapq import heappop, heappush
from typing import List


class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        cell_count = m * n
        target_cell = cell_count - 1
        infinity = 10**30
        distance = [infinity] * (2 * cell_count)
        distance[0] = 1
        heap = [(1, 0)]
        directions = ((0, 1, 0), (1, 0, 0), (0, -1, 1), (-1, 0, 1))

        while heap:
            cost, state = heappop(heap)
            if cost != distance[state]:
                continue

            cell = state >> 1
            if cell == target_cell:
                return cost

            row, column = divmod(cell, n)
            parity = state & 1
            next_parity = parity ^ 1
            current_penalty = penalty[row][column]

            wait_state = (cell << 1) | next_parity
            wait_cost = cost + current_penalty
            if wait_cost < distance[wait_state]:
                distance[wait_state] = wait_cost
                heappush(heap, (wait_cost, wait_state))

            for row_step, column_step, allowed_parity in directions:
                next_row = row + row_step
                next_column = column + column_step
                if not (0 <= next_row < m and 0 <= next_column < n):
                    continue

                next_cell = next_row * n + next_column
                next_state = (next_cell << 1) | next_parity
                move_cost = cost + (next_row + 1) * (next_column + 1)
                if parity != allowed_parity:
                    move_cost += current_penalty

                if move_cost < distance[next_state]:
                    distance[next_state] = move_cost
                    heappush(heap, (move_cost, next_state))

        return -1
