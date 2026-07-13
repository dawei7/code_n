"""Optimal solution for LeetCode 1324: Print Words Vertically."""


def solve(s: str) -> list[str]:
    words = s.split()
    width = max(len(word) for word in words)
    rows: list[str] = []
    for col in range(width):
        chars = [word[col] if col < len(word) else " " for word in words]
        rows.append("".join(chars).rstrip())
    return rows
