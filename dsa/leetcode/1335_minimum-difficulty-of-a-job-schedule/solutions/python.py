def solve(job_difficulty, d):
    n = len(job_difficulty)
    if n < d:
        return -1
    dp = job_difficulty[:]
    for i in range(n - 2, -1, -1):
        dp[i] = max(job_difficulty[i], dp[i + 1])

    for day in range(2, d + 1):
        next_dp = [float("inf")] * n
        for i in range(n - day + 1):
            hardest = 0
            for cut in range(i, n - day + 1):
                hardest = max(hardest, job_difficulty[cut])
                next_dp[i] = min(next_dp[i], hardest + dp[cut + 1])
        dp = next_dp
    return dp[0]
