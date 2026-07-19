from collections import Counter


def solve(text: str) -> int:
    counts = Counter(text)
    return min(
        counts["b"],
        counts["a"],
        counts["l"] // 2,
        counts["o"] // 2,
        counts["n"],
    )
