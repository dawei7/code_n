from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        differences = [first - second for first, second in zip(nums1, nums2)]
        coordinates = sorted(set(differences))
        tree = [0] * (len(coordinates) + 1)

        def query(index: int) -> int:
            total = 0
            while index > 0:
                total += tree[index]
                index -= index & -index
            return total

        def add(index: int) -> None:
            while index < len(tree):
                tree[index] += 1
                index += index & -index

        answer = 0
        for value in differences:
            answer += query(bisect_right(coordinates, value + diff))
            add(bisect_left(coordinates, value) + 1)

        return answer
