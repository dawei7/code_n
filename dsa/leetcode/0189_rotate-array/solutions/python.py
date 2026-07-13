def _reverse(nums: list[int], left: int, right: int) -> None:
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def solve(nums: list[int], k: int) -> None:
    k %= len(nums)
    _reverse(nums, 0, len(nums) - 1)
    _reverse(nums, 0, k - 1)
    _reverse(nums, k, len(nums) - 1)
