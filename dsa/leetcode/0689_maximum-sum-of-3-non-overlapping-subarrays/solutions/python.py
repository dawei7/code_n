def solve(nums: list[int], k: int) -> list[int]:
    window_count = len(nums) - k + 1
    window_sums = [0] * window_count
    current = sum(nums[:k])
    window_sums[0] = current
    for start in range(1, window_count):
        current += nums[start + k - 1] - nums[start - 1]
        window_sums[start] = current

    left = [0] * window_count
    for index in range(1, window_count):
        left[index] = index if window_sums[index] > window_sums[left[index - 1]] else left[index - 1]

    right = [0] * window_count
    right[-1] = window_count - 1
    for index in range(window_count - 2, -1, -1):
        right[index] = index if window_sums[index] >= window_sums[right[index + 1]] else right[index + 1]

    best_total = -1
    answer = []
    for middle in range(k, window_count - k):
        first = left[middle - k]
        third = right[middle + k]
        total = window_sums[first] + window_sums[middle] + window_sums[third]
        if total > best_total:
            best_total = total
            answer = [first, middle, third]
    return answer

