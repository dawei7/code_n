def solve(nums: list[int], k: int, maxChanges: int) -> int:
    ones = [i for i, value in enumerate(nums) if value]

    nearby = 0
    for i, value in enumerate(nums):
        if value:
            count = 1
            if i > 0 and nums[i - 1]:
                count += 1
            if i + 1 < len(nums) and nums[i + 1]:
                count += 1
            nearby = max(nearby, count)

    nearby = min(nearby, k)
    if maxChanges >= k - nearby:
        return max(0, nearby - 1) + 2 * (k - nearby)

    needed = k - maxChanges
    prefix = [0]
    for position in ones:
        prefix.append(prefix[-1] + position)

    best = float("inf")
    for left in range(len(ones) - needed + 1):
        right = left + needed
        mid = (left + right - 1) // 2
        median = ones[mid]

        cost = median * (mid - left) - (prefix[mid] - prefix[left])
        cost += (
            prefix[right]
            - prefix[mid + 1]
            - median * (right - mid - 1)
        )
        best = min(best, cost)

    return int(best) + 2 * maxChanges
