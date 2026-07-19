def solve(nums: list[int], k: int) -> int:
    mod = 10**9 + 7
    arr = sorted(nums)
    n = len(arr)

    diffs = sorted({arr[j] - arr[i] for i in range(n) for j in range(i + 1, n) if arr[j] > arr[i]})
    if not diffs:
        return 0

    def count_with_min_gap(gap: int) -> int:
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(n):
            dp[1][i] = 1

        for length in range(2, k + 1):
            prefix = 0
            left = 0
            for right in range(n):
                while left < right and arr[right] - arr[left] >= gap:
                    prefix = (prefix + dp[length - 1][left]) % mod
                    left += 1
                dp[length][right] = prefix

        return sum(dp[k]) % mod

    answer = 0
    previous = 0
    for gap in diffs:
        count = count_with_min_gap(gap)
        answer = (answer + (gap - previous) * count) % mod
        previous = gap

    return answer
