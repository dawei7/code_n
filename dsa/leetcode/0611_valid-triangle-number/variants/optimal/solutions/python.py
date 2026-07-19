def solve(nums: list[int]) -> int:
    values = sorted(nums)
    count = 0

    for largest in range(len(values) - 1, 1, -1):
        left = 0
        right = largest - 1
        while left < right:
            if values[left] + values[right] > values[largest]:
                count += right - left
                right -= 1
            else:
                left += 1

    return count
