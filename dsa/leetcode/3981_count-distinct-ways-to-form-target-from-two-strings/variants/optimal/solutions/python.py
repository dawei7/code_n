def solve(word1: str, word2: str, target: str) -> int:
    modulo = 1_000_000_007
    n1 = len(word1)
    n2 = len(word2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    dp[0][0] = 1

    for needed in target:
        next_dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for last2 in range(n2 + 1):
            prefix = 0
            for new1 in range(1, n1 + 1):
                prefix = (prefix + dp[new1 - 1][last2]) % modulo
                if word1[new1 - 1] == needed:
                    next_dp[new1][last2] = prefix

        for last1 in range(n1 + 1):
            prefix = 0
            for new2 in range(1, n2 + 1):
                prefix = (prefix + dp[last1][new2 - 1]) % modulo
                if word2[new2 - 1] == needed:
                    next_dp[last1][new2] = (
                        next_dp[last1][new2] + prefix
                    ) % modulo

        dp = next_dp

    return sum(
        dp[last1][last2]
        for last1 in range(1, n1 + 1)
        for last2 in range(1, n2 + 1)
    ) % modulo
