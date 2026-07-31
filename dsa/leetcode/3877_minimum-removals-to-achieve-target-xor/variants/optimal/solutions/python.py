def solve(nums: list[int], target: int) -> int:
    best = {0: 0}

    for value in nums:
        next_best = best.copy()

        for xor_value, kept in best.items():
            candidate = xor_value ^ value
            next_best[candidate] = max(next_best.get(candidate, -1), kept + 1)

        best = next_best

    kept = best.get(target, -1)
    return -1 if kept < 0 else len(nums) - kept
