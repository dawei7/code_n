def solve(k: int) -> str:
    return chr(ord("a") + (k - 1).bit_count())
