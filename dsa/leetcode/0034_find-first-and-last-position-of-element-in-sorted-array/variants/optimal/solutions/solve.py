def solve(nums: list[int], target: int) -> list[int]:
    def boundary(strict: bool) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target or (strict and nums[middle] == target):
                left = middle + 1
            else:
                right = middle
        return left

    first = boundary(False)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    return [first, boundary(True) - 1]
