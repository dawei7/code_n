from collections import Counter


def solve(nums: list[int]) -> int:
    total = sum(nums)
    counts = Counter(nums)
    answer = -10**9

    for outlier in counts:
        remaining = total - outlier
        if remaining % 2:
            continue

        sum_element = remaining // 2
        available = counts[sum_element] - (sum_element == outlier)
        if available > 0:
            answer = max(answer, outlier)

    return answer
