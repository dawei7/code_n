def solve(nums: list[int], target: int) -> int:
    unreachable = -1
    best_length = [unreachable] * (target + 1)
    best_length[0] = 0

    for value in nums:
        for total in range(target, value - 1, -1):
            previous = best_length[total - value]
            if previous != unreachable:
                best_length[total] = max(best_length[total], previous + 1)

    return best_length[target]
