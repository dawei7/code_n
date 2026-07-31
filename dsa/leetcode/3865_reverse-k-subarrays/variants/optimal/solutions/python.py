def solve(nums: list[int], k: int) -> list[int]:
    block_size = len(nums) // k

    for block_start in range(0, len(nums), block_size):
        left = block_start
        right = block_start + block_size - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums
