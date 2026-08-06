def solve(nums1: list[int], nums2: list[int]) -> list[int]:
    index_by_value = {value: nums2_position for nums2_position, value in enumerate(nums2)}
    return [index_by_value[value] for value in nums1]
