from collections import defaultdict


def solve(nums: list[int], k: int) -> int:
    target = []
    remaining = k

    for prime in (2, 3, 5):
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        target.append(exponent)

    if remaining != 1:
        return 0

    factors = (
        (0, 0, 0),
        (0, 0, 0),
        (1, 0, 0),
        (0, 1, 0),
        (2, 0, 0),
        (0, 0, 1),
        (1, 1, 0),
    )
    ways = {(0, 0, 0): 1}

    for num in nums:
        dx, dy, dz = factors[num]
        next_ways = defaultdict(int)

        for (x, y, z), count in ways.items():
            next_ways[(x + dx, y + dy, z + dz)] += count
            next_ways[(x - dx, y - dy, z - dz)] += count
            next_ways[(x, y, z)] += count

        ways = next_ways

    return ways.get(tuple(target), 0)
