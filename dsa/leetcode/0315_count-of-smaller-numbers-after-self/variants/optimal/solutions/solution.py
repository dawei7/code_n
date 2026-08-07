from typing import List


def _count_smaller(nums: List[int]) -> List[int]:
    ranks = {value: rank for rank, value in enumerate(sorted(set(nums)), 1)}
    tree = [0] * (len(ranks) + 1)

    def prefix_sum(index: int) -> int:
        total = 0
        while index > 0:
            total += tree[index]
            index -= index & -index
        return total

    def add(index: int) -> None:
        while index < len(tree):
            tree[index] += 1
            index += index & -index

    answer = [0] * len(nums)
    for index in range(len(nums) - 1, -1, -1):
        rank = ranks[nums[index]]
        answer[index] = prefix_sum(rank - 1)
        add(rank)
    return answer


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        return _count_smaller(nums)
