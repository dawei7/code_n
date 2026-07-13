from itertools import accumulate


def solve(nums: list[int], k: int, maxChanges: int) -> int:
    ones = [i for i, value in enumerate(nums) if value == 1]
    if not ones:
        return k * 2

    adjacent_pickups = 0
    n = len(nums)
    for index in ones:
        count = 1
        if index > 0 and nums[index - 1] == 1:
            count += 1
        if index + 1 < n and nums[index + 1] == 1:
            count += 1
        adjacent_pickups = max(adjacent_pickups, count)

    adjacent_pickups = min(adjacent_pickups, k)
    if adjacent_pickups + maxChanges >= k:
        return adjacent_pickups - 1 + (k - adjacent_pickups) * 2

    needed_existing = k - maxChanges
    prefix = list(accumulate(ones, initial=0))
    best = 10**30

    for left in range(len(ones) - needed_existing + 1):
        right = left + needed_existing - 1
        mid = (left + right) // 2
        center = ones[mid]

        left_cost = center * (mid - left + 1) - (prefix[mid + 1] - prefix[left])
        right_cost = (prefix[right + 1] - prefix[mid]) - center * (right - mid + 1)
        best = min(best, left_cost + right_cost)

    return best + maxChanges * 2
