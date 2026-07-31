def solve(s: str) -> int:
    n = len(s)
    dp = list(range(n + 1))

    for end in range(1, n + 1):
        counts = [0] * 26
        distinct = 0
        maximum = 0

        for start in range(end - 1, -1, -1):
            index = ord(s[start]) - ord("a")
            if counts[index] == 0:
                distinct += 1
            counts[index] += 1
            maximum = max(maximum, counts[index])

            if end - start == distinct * maximum:
                dp[end] = min(dp[end], dp[start] + 1)

    return dp[n]
