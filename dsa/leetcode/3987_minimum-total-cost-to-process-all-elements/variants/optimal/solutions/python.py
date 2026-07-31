MOD = 1_000_000_007


def solve(nums: list[int], k: int) -> int:
    """Return the minimum resource-operation cost modulo MOD."""

    total_demand = 0
    for value in nums:
        total_demand += value

    operations = (total_demand - 1) // k
    return operations * (operations + 1) // 2 % MOD
