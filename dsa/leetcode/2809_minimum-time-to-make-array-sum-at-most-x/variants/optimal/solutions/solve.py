def solve(nums1: list[int], nums2: list[int], x: int) -> int:
    pairs = sorted(zip(nums2, nums1))
    n = len(nums1)
    reduction = [0] * (n + 1)

    for growth, initial in pairs:
        for operations in range(n, 0, -1):
            reduction[operations] = max(
                reduction[operations],
                reduction[operations - 1] + initial + growth * operations,
            )

    initial_sum = sum(nums1)
    growth_sum = sum(nums2)
    for seconds in range(n + 1):
        if initial_sum + growth_sum * seconds - reduction[seconds] <= x:
            return seconds
    return -1
