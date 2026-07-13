def solve(nums: list[int]) -> list[int]:
    low = current = 0
    high = len(nums) - 1
    while current <= high:
        if nums[current] == 0:
            nums[low], nums[current] = nums[current], nums[low]
            low += 1
            current += 1
        elif nums[current] == 1:
            current += 1
        else:
            nums[current], nums[high] = nums[high], nums[current]
            high -= 1
    return nums
