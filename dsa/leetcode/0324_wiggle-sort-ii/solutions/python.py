def _select(nums: list[int], rank: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        pivot = sorted((nums[left], nums[middle], nums[right]))[1]
        lower = scan = left
        upper = right
        while scan <= upper:
            if nums[scan] < pivot:
                nums[lower], nums[scan] = nums[scan], nums[lower]
                lower += 1
                scan += 1
            elif nums[scan] > pivot:
                nums[scan], nums[upper] = nums[upper], nums[scan]
                upper -= 1
            else:
                scan += 1
        if rank < lower:
            right = lower - 1
        elif rank > upper:
            left = upper + 1
        else:
            return pivot
    raise RuntimeError("unreachable rank")


def solve(nums: list[int]) -> None:
    length = len(nums)
    if length < 2:
        return
    median = _select(nums, length // 2)

    def virtual(index: int) -> int:
        return (1 + 2 * index) % (length | 1)

    lower = scan = 0
    upper = length - 1
    while scan <= upper:
        mapped = virtual(scan)
        if nums[mapped] > median:
            low_mapped = virtual(lower)
            nums[low_mapped], nums[mapped] = nums[mapped], nums[low_mapped]
            lower += 1
            scan += 1
        elif nums[mapped] < median:
            high_mapped = virtual(upper)
            nums[mapped], nums[high_mapped] = nums[high_mapped], nums[mapped]
            upper -= 1
        else:
            scan += 1
