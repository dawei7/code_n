from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        normalized = [value // k for value in nums]
        coordinates = sorted(set(normalized))
        rank = {value: index for index, value in enumerate(coordinates)}

        left_child = [0]
        right_child = [0]
        counts = [0]
        totals = [0]

        def add(previous: int, low: int, high: int, position: int, value: int) -> int:
            node = len(counts)
            left_child.append(left_child[previous])
            right_child.append(right_child[previous])
            counts.append(counts[previous] + 1)
            totals.append(totals[previous] + value)
            if low != high:
                middle = (low + high) // 2
                if position <= middle:
                    left_child[node] = add(left_child[previous], low, middle, position, value)
                else:
                    right_child[node] = add(right_child[previous], middle + 1, high, position, value)
            return node

        roots = [0]
        maximum_rank = len(coordinates) - 1
        for value in normalized:
            roots.append(add(roots[-1], 0, maximum_rank, rank[value], value))

        remainder_changes = [0] * len(nums)
        for index in range(1, len(nums)):
            remainder_changes[index] = remainder_changes[index - 1] + (nums[index] % k != nums[index - 1] % k)

        answer = []
        for query_left, query_right in queries:
            if remainder_changes[query_right] != remainder_changes[query_left]:
                answer.append(-1)
                continue

            older_root = roots[query_left]
            newer_root = roots[query_right + 1]
            length = query_right - query_left + 1
            order = (length + 1) // 2
            low = 0
            high = maximum_rank
            below_count = 0
            below_sum = 0
            older_node = older_root
            newer_node = newer_root

            while low != high:
                middle = (low + high) // 2
                older_left = left_child[older_node]
                newer_left = left_child[newer_node]
                left_count = counts[newer_left] - counts[older_left]
                if order <= left_count:
                    older_node = older_left
                    newer_node = newer_left
                    high = middle
                else:
                    below_count += left_count
                    below_sum += totals[newer_left] - totals[older_left]
                    order -= left_count
                    older_node = right_child[older_node]
                    newer_node = right_child[newer_node]
                    low = middle + 1

            median = coordinates[low]
            median_count = counts[newer_node] - counts[older_node]
            median_sum = totals[newer_node] - totals[older_node]
            left_count = below_count + median_count
            left_sum = below_sum + median_sum
            range_sum = totals[newer_root] - totals[older_root]
            right_count = length - left_count
            right_sum = range_sum - left_sum
            answer.append(median * left_count - left_sum + right_sum - median * right_count)

        return answer
