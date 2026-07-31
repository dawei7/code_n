def solve(nums: list[int], k: int) -> int:
    if 0 in nums:
        return 1

    groups = 1
    product = nums[0]

    for value in nums[1:]:
        if product <= k // value:
            product *= value
        else:
            groups += 1
            product = value

    return groups
