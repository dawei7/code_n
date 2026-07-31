from collections import defaultdict
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        parent = list(range(len(nums)))
        size = [1] * len(nums)

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for left, right in swaps:
            left_root = find(left)
            right_root = find(right)
            if left_root == right_root:
                continue
            if size[left_root] < size[right_root]:
                left_root, right_root = right_root, left_root
            parent[right_root] = left_root
            size[left_root] += size[right_root]

        values_by_root = defaultdict(list)
        even_positions_by_root = defaultdict(int)
        for index, value in enumerate(nums):
            root = find(index)
            values_by_root[root].append(value)
            if index % 2 == 0:
                even_positions_by_root[root] += 1

        answer = 0
        for root, values in values_by_root.items():
            values.sort()
            positive_count = even_positions_by_root[root]
            positive_start = len(values) - positive_count
            answer += 2 * sum(values[positive_start:]) - sum(values)

        return answer
