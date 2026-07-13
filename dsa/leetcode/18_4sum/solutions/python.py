def solve(nums: list[int], target: int) -> list[list[int]]:
    values = sorted(nums)
    result: list[list[int]] = []
    for first in range(len(values) - 3):
        if first and values[first] == values[first - 1]:
            continue
        for second in range(first + 1, len(values) - 2):
            if second > first + 1 and values[second] == values[second - 1]:
                continue
            left, right = second + 1, len(values) - 1
            while left < right:
                total = values[first] + values[second] + values[left] + values[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    result.append([values[first], values[second], values[left], values[right]])
                    left_value, right_value = values[left], values[right]
                    while left < right and values[left] == left_value:
                        left += 1
                    while left < right and values[right] == right_value:
                        right -= 1
    return result
