class Solution:
    def houseOfCards(self, n: int) -> int:
        ways = [0] * (n + 1)
        ways[0] = 1

        row_cost = 2
        while row_cost <= n:
            for cards in range(n, row_cost - 1, -1):
                ways[cards] += ways[cards - row_cost]
            row_cost += 3

        return ways[n]
