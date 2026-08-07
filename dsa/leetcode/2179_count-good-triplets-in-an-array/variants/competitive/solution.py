from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        position = [0] * n
        for index, value in enumerate(nums2):
            position[value] = index

        tree = [0] * (n + 1)

        def prefix_count(end: int) -> int:
            total = 0
            while end > 0:
                total += tree[end]
                end -= end & -end
            return total

        def add(index: int) -> None:
            index += 1
            while index <= n:
                tree[index] += 1
                index += index & -index

        answer = 0
        for first_index, value in enumerate(nums1):
            second_index = position[value]
            earlier_smaller = prefix_count(second_index)
            earlier_larger = first_index - earlier_smaller
            later_larger = n - 1 - second_index - earlier_larger
            answer += earlier_smaller * later_larger
            add(second_index)

        return answer
