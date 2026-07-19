def solve(prizePositions: list[int], k: int) -> int:
    n = len(prizePositions)

    # dp[i] will store the max prizes covered by a segment of length k ending at or before index i
    # count[i] will store the max prizes covered by a segment of length k ending exactly at index i
    count = [0] * n
    left = 0
    for right in range(n):
        while prizePositions[right] - prizePositions[left] > k:
            left += 1
        count[right] = right - left + 1

    # dp[i] stores the max prizes covered by a segment ending at or before index i
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i], count[i])

    ans = 0
    left = 0
    # For each segment ending at 'right', find the best non-overlapping segment ending at 'left-1'
    for right in range(n):
        while prizePositions[right] - prizePositions[left] > k:
            left += 1
        # Current segment covers [left, right]
        # Best previous segment covers up to index left-1
        current_prizes = (right - left + 1) + dp[left]
        ans = max(ans, current_prizes)

    return ans
