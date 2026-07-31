def solve(n: int) -> list[int]:
    counts = [0, 0]
    index = 0

    while n:
        counts[index & 1] += n & 1
        n >>= 1
        index += 1

    return counts
