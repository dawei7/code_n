def solve(s: str) -> int:
    modulus = 1_000_000_007
    moves = {"F": 0, "W": 1, "E": 2}
    n = len(s)
    offset = n
    width = 2 * n + 1

    def score(bob: int, alice: int) -> int:
        if bob == alice:
            return 0
        return 1 if (bob - alice) % 3 == 1 else -1

    dp = [[0] * width for _ in range(3)]
    alice = moves[s[0]]
    for bob in range(3):
        dp[bob][offset + score(bob, alice)] = 1

    for round_index in range(1, n):
        alice = moves[s[round_index]]
        next_dp = [[0] * width for _ in range(3)]

        for previous in range(3):
            for difference in range(-round_index, round_index + 1):
                ways = dp[previous][offset + difference]
                if ways == 0:
                    continue
                for bob in range(3):
                    if bob != previous:
                        index = offset + difference + score(bob, alice)
                        next_dp[bob][index] = (next_dp[bob][index] + ways) % modulus

        dp = next_dp

    return sum(dp[last][offset + difference] for last in range(3) for difference in range(1, n + 1)) % modulus
