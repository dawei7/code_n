from bisect import bisect_right


def solve(start_time, end_time, profit):
    jobs = sorted(zip(end_time, start_time, profit))
    ends = [0]
    dp = [0]
    for end, start, gain in jobs:
        best = dp[bisect_right(ends, start) - 1] + gain
        if best > dp[-1]:
            ends.append(end)
            dp.append(best)
    return dp[-1]
