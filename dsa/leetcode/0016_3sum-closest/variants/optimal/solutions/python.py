def solve(nums: list[int], target: int) -> int:
    values = sorted(nums)
    closest = values[0] + values[1] + values[2]
    for index in range(len(values) - 2):
        left, right = index + 1, len(values) - 1
        while left < right:
            total = values[index] + values[left] + values[right]
            if abs(total - target) < abs(closest - target):
                closest = total
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return target
    return closest
