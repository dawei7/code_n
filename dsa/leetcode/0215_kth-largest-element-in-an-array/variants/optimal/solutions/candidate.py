from random import randrange


def solve(nums: list[int], k: int) -> int:
    target = len(nums) - k
    left, right = 0, len(nums) - 1
    while True:
        pivot = sorted(nums[randrange(left, right + 1)] for _ in range(3))[1]
        lower, i, upper = left, left, right
        while i <= upper:
            if nums[i] < pivot:
                nums[lower], nums[i] = nums[i], nums[lower]
                lower += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[upper] = nums[upper], nums[i]
                upper -= 1
            else:
                i += 1
        if target < lower:
            right = lower - 1
        elif target > upper:
            left = upper + 1
        else:
            return pivot
