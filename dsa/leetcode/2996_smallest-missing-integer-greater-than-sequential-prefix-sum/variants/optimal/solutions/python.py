def solve(nums):
    prefix_sum = nums[0]
    for index in range(1, len(nums)):
        if nums[index] != nums[index - 1] + 1:
            break
        prefix_sum += nums[index]

    present = set(nums)
    while prefix_sum in present:
        prefix_sum += 1
    return prefix_sum
