def solve(arr: list[int]) -> int:
    length = len(arr)
    dp = [[0] * length for _ in range(length)]
    for index in range(length):
        dp[index][index] = 1

    for width in range(2, length + 1):
        for left in range(length - width + 1):
            right = left + width - 1
            dp[left][right] = 1 + dp[left + 1][right]
            if arr[left] == arr[left + 1]:
                dp[left][right] = min(
                    dp[left][right],
                    1 + (dp[left + 2][right] if left + 2 <= right else 0),
                )
            for middle in range(left + 2, right + 1):
                if arr[left] == arr[middle]:
                    suffix = dp[middle + 1][right] if middle < right else 0
                    dp[left][right] = min(
                        dp[left][right], dp[left + 1][middle - 1] + suffix
                    )
    return dp[0][length - 1]
