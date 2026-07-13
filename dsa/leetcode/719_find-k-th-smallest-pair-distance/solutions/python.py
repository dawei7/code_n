def solve(nums: list[int], k: int) -> int:
    values = sorted(nums)
    low = 0
    high = values[-1] - values[0]

    while low < high:
        middle = (low + high) // 2
        count = 0
        left = 0

        for right, value in enumerate(values):
            while value - values[left] > middle:
                left += 1
            count += right - left

        if count >= k:
            high = middle
        else:
            low = middle + 1

    return low
