from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mine_cells = {tuple(mine) for mine in mines}
        orders = [[n] * n for _ in range(n)]

        for row in range(n):
            run = 0
            for column in range(n):
                run = 0 if (row, column) in mine_cells else run + 1
                orders[row][column] = min(orders[row][column], run)

            run = 0
            for column in range(n - 1, -1, -1):
                run = 0 if (row, column) in mine_cells else run + 1
                orders[row][column] = min(orders[row][column], run)

        for column in range(n):
            run = 0
            for row in range(n):
                run = 0 if (row, column) in mine_cells else run + 1
                orders[row][column] = min(orders[row][column], run)

            run = 0
            for row in range(n - 1, -1, -1):
                run = 0 if (row, column) in mine_cells else run + 1
                orders[row][column] = min(orders[row][column], run)

        return max(map(max, orders), default=0)
