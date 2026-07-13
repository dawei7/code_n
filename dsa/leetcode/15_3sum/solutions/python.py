def solve(nums: list[int]) -> list[list[int]]:
    values = sorted(nums)
    result: list[list[int]] = []
    for index, fixed in enumerate(values):
        if fixed > 0:
            break
        if index > 0 and fixed == values[index - 1]:
            continue
        left, right = index + 1, len(values) - 1
        while left < right:
            total = fixed + values[left] + values[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([fixed, values[left], values[right]])
                left_value, right_value = values[left], values[right]
                while left < right and values[left] == left_value:
                    left += 1
                while left < right and values[right] == right_value:
                    right -= 1
    return result
