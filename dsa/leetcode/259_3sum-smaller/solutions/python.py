def solve(nums: list[int], target: int) -> int:
    values = sorted(nums)
    count = 0
    for first in range(len(values) - 2):
        left = first + 1
        right = len(values) - 1
        while left < right:
            if values[first] + values[left] + values[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count
