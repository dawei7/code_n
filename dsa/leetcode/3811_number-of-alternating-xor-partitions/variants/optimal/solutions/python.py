def solve(nums: list[int], target1: int, target2: int) -> int:
    mod = 1_000_000_007
    even_by_prefix = {0: 1}
    odd_by_prefix: dict[int, int] = {}
    prefix = 0
    even = odd = 0

    for value in nums:
        prefix ^= value
        odd = even_by_prefix.get(prefix ^ target1, 0)
        even = odd_by_prefix.get(prefix ^ target2, 0)
        odd_by_prefix[prefix] = (odd_by_prefix.get(prefix, 0) + odd) % mod
        even_by_prefix[prefix] = (even_by_prefix.get(prefix, 0) + even) % mod

    return (odd + even) % mod
