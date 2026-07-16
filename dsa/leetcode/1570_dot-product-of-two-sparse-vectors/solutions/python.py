def solve(nums1: list[int], nums2: list[int]) -> int:
    first = {index: value for index, value in enumerate(nums1) if value != 0}
    second = {index: value for index, value in enumerate(nums2) if value != 0}

    if len(first) > len(second):
        first, second = second, first

    return sum(value * second.get(index, 0) for index, value in first.items())
