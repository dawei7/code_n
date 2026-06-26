"""Optimal solution for LeetCode 1105: Filling Bookcase Shelves."""


def solve(books: list[list[int]], shelf_width: int) -> int:
    n = len(books)
    dp = [0] + [10**18] * n
    for i in range(1, n + 1):
        width = 0
        height = 0
        for j in range(i, 0, -1):
            width += books[j - 1][0]
            if width > shelf_width:
                break
            height = max(height, books[j - 1][1])
            dp[i] = min(dp[i], dp[j - 1] + height)
    return dp[n]
