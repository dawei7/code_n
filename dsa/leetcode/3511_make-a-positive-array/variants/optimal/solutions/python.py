def solve(nums: list[int]) -> int:
    operations = 0
    last_replaced = -1

    for right in range(2, len(nums)):
        total = 0
        for left in range(right, max(-1, right - 5), -1):
            total += nums[left]
            if right - left >= 2 and last_replaced < left and total <= 0:
                operations += 1
                last_replaced = right
                break

    return operations
