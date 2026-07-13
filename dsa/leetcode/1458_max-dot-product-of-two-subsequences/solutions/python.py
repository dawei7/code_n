def solve(nums1, nums2):
    rows, cols = len(nums1), len(nums2)
    dp = [[float("-inf")] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            product = nums1[i - 1] * nums2[j - 1]
            dp[i][j] = max(product, product + max(0, dp[i - 1][j - 1]), dp[i - 1][j], dp[i][j - 1])
    return dp[rows][cols]
