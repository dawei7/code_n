def solve(nums: list[int], x: int) -> int:
    unreachable = -(10**30)
    best = [unreachable, unreachable]
    best[nums[0] % 2] = nums[0]

    for value in nums[1:]:
        parity = value % 2
        best[parity] = max(
            best[parity] + value,
            best[1 - parity] + value - x,
        )

    return max(best)
