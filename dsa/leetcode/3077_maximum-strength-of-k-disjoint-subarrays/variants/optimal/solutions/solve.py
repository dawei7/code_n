def solve(nums: list[int], k: int) -> int:
    negative_infinity = -(10**30)
    best = [negative_infinity] * (k + 1)
    ending = [negative_infinity] * (k + 1)
    best[0] = 0

    for value in nums:
        for used in range(k, 0, -1):
            weight = k - used + 1
            if used % 2 == 0:
                weight = -weight
            contribution = weight * value
            ending[used] = max(
                ending[used] + contribution,
                best[used - 1] + contribution,
            )
            best[used] = max(best[used], ending[used])

    return best[k]
