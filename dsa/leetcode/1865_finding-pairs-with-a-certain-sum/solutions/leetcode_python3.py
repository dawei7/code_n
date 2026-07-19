from collections import Counter
from typing import List


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_frequency = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_value = self.nums2[index]
        self.nums2_frequency[old_value] -= 1
        self.nums2[index] += val
        self.nums2_frequency[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(
            self.nums2_frequency[tot - value] for value in self.nums1
        )
