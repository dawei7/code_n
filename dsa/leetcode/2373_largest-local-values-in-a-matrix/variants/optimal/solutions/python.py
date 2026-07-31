from __future__ import annotations


def solve(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    return [
        [
            max(
                grid[row + dr][col + dc]
                for dr in range(3)
                for dc in range(3)
            )
            for col in range(n - 2)
        ]
        for row in range(n - 2)
    ]
