from math import isqrt


def solve(nums: list[int]) -> int:
    mod = 1_000_000_007
    maximum = max(nums)

    phi = list(range(maximum + 1))
    for prime in range(2, maximum + 1):
        if phi[prime] == prime:
            for multiple in range(prime, maximum + 1, prime):
                phi[multiple] -= phi[multiple] // prime

    trees: dict[int, list[int]] = {}
    divisible_counts = [0] * (maximum + 1)

    def extend(divisor: int, value: int) -> None:
        tree = trees.get(divisor)
        if tree is None:
            tree = [0] * (maximum // divisor + 1)
            trees[divisor] = tree

        quotient = value // divisor
        prefix = 0
        index = quotient - 1
        while index:
            prefix += tree[index]
            if prefix >= mod:
                prefix -= mod
            index -= index & -index

        ways = prefix + 1
        if ways == mod:
            ways = 0

        divisible_counts[divisor] += ways
        if divisible_counts[divisor] >= mod:
            divisible_counts[divisor] -= mod

        index = quotient
        while index < len(tree):
            tree[index] += ways
            if tree[index] >= mod:
                tree[index] -= mod
            index += index & -index

    for value in nums:
        for divisor in range(1, isqrt(value) + 1):
            if value % divisor == 0:
                extend(divisor, value)
                other = value // divisor
                if other != divisor:
                    extend(other, value)

    return sum(
        phi[divisor] * divisible_counts[divisor]
        for divisor in range(1, maximum + 1)
    ) % mod
