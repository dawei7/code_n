def solve(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result: list[list[int]] = []
    for i, fixed in enumerate(nums):
        if fixed > 0:
            break
        if i > 0 and fixed == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = fixed + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([fixed, nums[left], nums[right]])
                left_value, right_value = nums[left], nums[right]
                while left < right and nums[left] == left_value:
                    left += 1
                while left < right and nums[right] == right_value:
                    right -= 1

    return result
