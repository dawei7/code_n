def solve(nums: list[int]) -> int:
    n = len(nums)
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)

    best = 0
    odd = [0] * n
    left = 0
    right = -1

    for center in range(n):
        radius = 1 if center > right else min(odd[left + right - center], right - center + 1)
        while center - radius >= 0 and center + radius < n and nums[center - radius] == nums[center + radius]:
            radius += 1

        odd[center] = radius
        start = center - radius + 1
        end = center + radius
        best = max(best, prefix[end] - prefix[start])

        if center + radius - 1 > right:
            left = center - radius + 1
            right = center + radius - 1

    even = [0] * n
    left = 0
    right = -1

    for center in range(n):
        radius = 0 if center > right else min(even[left + right - center + 1], right - center + 1)
        while center - radius - 1 >= 0 and center + radius < n and nums[center - radius - 1] == nums[center + radius]:
            radius += 1

        even[center] = radius
        if radius:
            best = max(
                best,
                prefix[center + radius] - prefix[center - radius],
            )

        if center + radius - 1 > right:
            left = center - radius
            right = center + radius - 1

    return best
