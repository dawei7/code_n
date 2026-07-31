def solve(nums1: list[int], nums2: list[int]) -> int:
    first_index: dict[int, int] = {}
    for index, value in enumerate(nums1):
        first_index.setdefault(value, index)

    answer = 2 * len(nums1)
    for index, value in enumerate(nums2):
        if value in first_index:
            answer = min(answer, first_index[value] + index)

    return -1 if answer == 2 * len(nums1) else answer
