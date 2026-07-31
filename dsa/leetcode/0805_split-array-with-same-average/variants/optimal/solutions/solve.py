def solve(nums: list[int]) -> bool:
    n = len(nums)
    if n < 2:
        return False

    total = sum(nums)
    if not any((total * size) % n == 0 for size in range(1, n // 2 + 1)):
        return False

    adjusted = [value * n - total for value in nums]
    middle = n // 2
    left_values = adjusted[:middle]
    right_values = adjusted[middle:]

    def subset_sums(values: list[int]) -> list[int]:
        sums = [0] * (1 << len(values))
        for mask in range(1, len(sums)):
            bit = mask & -mask
            index = bit.bit_length() - 1
            sums[mask] = sums[mask ^ bit] + values[index]
        return sums

    left = subset_sums(left_values)
    left_full_mask = len(left) - 1
    left_nonempty = set(left[1:])
    if 0 in left_nonempty:
        return True
    left_nonempty_nonfull = set(left[1:left_full_mask])

    right = subset_sums(right_values)
    right_full_mask = len(right) - 1
    for mask in range(1, len(right)):
        subset_sum = right[mask]
        if subset_sum == 0:
            return True
        candidates = left_nonempty_nonfull if mask == right_full_mask else left_nonempty
        if -subset_sum in candidates:
            return True
    return False
