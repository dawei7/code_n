def solve(n: int, k: int) -> int:
    modulus = 1_000_000_007
    ways = [0] * (k + 1)
    ways[0] = 1

    for candies in range(1, n + 1):
        for bags in range(min(candies, k), 0, -1):
            ways[bags] = (ways[bags - 1] + bags * ways[bags]) % modulus
        ways[0] = 0

    return ways[k]
