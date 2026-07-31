def solve(nums: list[int], p: int) -> int:
    target = sum(nums) % p
    if target == 0:
        return 0

    latest = {0: -1}
    prefix = 0
    best = len(nums)

    for index, value in enumerate(nums):
        prefix = (prefix + value) % p
        needed = (prefix - target) % p
        if needed in latest:
            best = min(best, index - latest[needed])
        latest[prefix] = index

    return best if best < len(nums) else -1
