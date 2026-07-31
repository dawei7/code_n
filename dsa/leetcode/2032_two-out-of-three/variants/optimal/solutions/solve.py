from collections import Counter


def solve(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    appearances: Counter[int] = Counter()
    for values in (nums1, nums2, nums3):
        for value in set(values):
            appearances[value] += 1
    return [value for value, count in appearances.items() if count >= 2]
