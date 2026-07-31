def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    if k == 0:
        return 0
    if k > n // 2:
        return -1

    def peak_cost(index: int) -> int:
        required = max(nums[(index - 1) % n], nums[(index + 1) % n]) + 1
        return max(0, required - nums[index])

    infinity = 10**30

    def path_cost(left: int, right: int, picks: int) -> int:
        if picks == 0:
            return 0
        if left > right or picks > (right - left + 2) // 2:
            return infinity

        skip = [infinity] * (picks + 1)
        take = [infinity] * (picks + 1)
        skip[0] = 0
        processed = 0

        for index in range(left, right + 1):
            upper = min(picks, (processed + 2) // 2)
            weight = peak_cost(index)
            for count in range(upper, 0, -1):
                old_take = take[count]
                take[count] = skip[count - 1] + weight
                skip[count] = min(skip[count], old_take)
            processed += 1

        return min(skip[picks], take[picks])

    without_first = path_cost(1, n - 1, k)
    with_first = peak_cost(0) + path_cost(2, n - 2, k - 1)
    return min(without_first, with_first)
