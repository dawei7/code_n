def solve(nums: list[int]) -> int:
    total = 0

    for left in range(len(nums)):
        distinct: set[int] = set()
        for right in range(left, len(nums)):
            distinct.add(nums[right])
            count = len(distinct)
            total += count * count

    return total
