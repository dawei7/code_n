def solve(stone_value):
    n = len(stone_value)
    if n <= 1:
        return 0
    prefix = [0]
    for value in stone_value:
        prefix.append(prefix[-1] + value)

    def interval_sum(left, right):
        return prefix[right + 1] - prefix[left]

    dp = [[0] * n for _ in range(n)]
    best_left = [[0] * n for _ in range(n)]
    best_right = [[0] * n for _ in range(n)]
    for index, value in enumerate(stone_value):
        best_left[index][index] = value
        best_right[index][index] = value

    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            total = interval_sum(left, right)
            best = 0

            lo, hi = left, right - 1
            last_left_not_greater = left - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if 2 * interval_sum(left, mid) <= total:
                    last_left_not_greater = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            if last_left_not_greater >= left:
                best = max(best, best_left[left][last_left_not_greater])

            lo, hi = left, right - 1
            first_left_not_less = right
            while lo <= hi:
                mid = (lo + hi) // 2
                if 2 * interval_sum(left, mid) >= total:
                    first_left_not_less = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            if first_left_not_less <= right - 1:
                best = max(best, best_right[first_left_not_less + 1][right])

            dp[left][right] = best
            best_left[left][right] = max(best_left[left][right - 1], best + total)
            best_right[left][right] = max(best_right[left + 1][right], best + total)
    return dp[0][n - 1]
