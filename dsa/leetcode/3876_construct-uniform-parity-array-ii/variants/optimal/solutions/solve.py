def solve(nums1: list[int]) -> bool:
    smallest = nums1[0]
    has_odd = False

    for value in nums1:
        smallest = min(smallest, value)
        has_odd = has_odd or value % 2 == 1

    return smallest % 2 == 1 or not has_odd
