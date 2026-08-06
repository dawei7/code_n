def solve(nums: list[int]) -> int:
    values = iter(nums)
    ending_here = best = next(values)
    for x in values:
        ending_here = max(x, ending_here + x)
        best = max(best, ending_here)
    return best
