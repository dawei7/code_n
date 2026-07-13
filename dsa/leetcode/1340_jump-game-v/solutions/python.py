from functools import lru_cache


def solve(arr, d):
    n = len(arr)

    @lru_cache(None)
    def dp(i):
        best = 1
        for direction in (-1, 1):
            for step in range(1, d + 1):
                j = i + direction * step
                if not (0 <= j < n) or arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dp(j))
        return best

    return max(dp(i) for i in range(n))
