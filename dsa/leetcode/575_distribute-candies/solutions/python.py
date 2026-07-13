def solve(candyType: list[int]) -> int:
    """Return the most distinct types possible in an equal half-share."""
    return min(len(set(candyType)), len(candyType) // 2)

