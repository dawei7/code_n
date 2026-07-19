def solve(nums1: list[int], nums2: list[int]) -> int:
    earliest = {0: -1}
    difference = 0
    widest = 0

    for index, (left, right) in enumerate(zip(nums1, nums2)):
        difference += left - right
        if difference in earliest:
            widest = max(widest, index - earliest[difference])
        else:
            earliest[difference] = index

    return widest
