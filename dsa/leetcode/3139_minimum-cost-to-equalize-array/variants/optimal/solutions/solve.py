def solve(nums: list[int], cost1: int, cost2: int) -> int:
    mod = 10**9 + 7
    n = len(nums)
    minimum = min(nums)
    maximum = max(nums)
    total = sum(nums)
    deficit_at_maximum = n * maximum - total

    if n <= 2 or cost2 >= 2 * cost1:
        return deficit_at_maximum * cost1 % mod

    balance = max(
        maximum,
        (total - 2 * minimum + n - 3) // (n - 2),
    )

    def cost(target: int) -> int:
        deficit = n * target - total
        largest = target - minimum
        pairs = min(deficit // 2, deficit - largest)
        singles = deficit - 2 * pairs
        return pairs * cost2 + singles * cost1

    candidates = {
        maximum,
        max(maximum, balance - 1),
        balance,
        balance + 1,
    }
    return min(cost(target) for target in candidates) % mod
