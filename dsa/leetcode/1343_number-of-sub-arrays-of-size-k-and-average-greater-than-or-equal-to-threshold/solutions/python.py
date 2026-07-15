"""Optimal app-local solution for LeetCode 1343."""


def solve(arr, k, threshold):
    target = k * threshold
    window_sum = sum(arr[:k])
    qualifying = int(window_sum >= target)

    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[right - k]
        if window_sum >= target:
            qualifying += 1

    return qualifying
