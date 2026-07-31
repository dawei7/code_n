from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        minimum = [0] * (4 * n)
        maximum = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node: int, change: int) -> None:
            minimum[node] += change
            maximum[node] += change
            lazy[node] += change

        def push(node: int) -> None:
            if lazy[node] != 0:
                apply(node * 2, lazy[node])
                apply(node * 2 + 1, lazy[node])
                lazy[node] = 0

        def add(
            node: int,
            left: int,
            right: int,
            query_left: int,
            query_right: int,
            change: int,
        ) -> None:
            if query_left <= left and right <= query_right:
                apply(node, change)
                return

            push(node)
            middle = (left + right) // 2
            if query_left <= middle:
                add(node * 2, left, middle, query_left, query_right, change)
            if query_right > middle:
                add(node * 2 + 1, middle + 1, right, query_left, query_right, change)
            minimum[node] = min(minimum[node * 2], minimum[node * 2 + 1])
            maximum[node] = max(maximum[node * 2], maximum[node * 2 + 1])

        def first_zero(node: int, left: int, right: int, limit: int) -> int:
            if left > limit or minimum[node] > 0 or maximum[node] < 0:
                return -1
            if left == right:
                return left

            push(node)
            middle = (left + right) // 2
            answer = first_zero(node * 2, left, middle, limit)
            if answer != -1:
                return answer
            return first_zero(node * 2 + 1, middle + 1, right, limit)

        last_position = [-1] * 100001
        longest = 0

        for right, value in enumerate(nums):
            change = 1 if value % 2 == 0 else -1
            add(
                1,
                0,
                n - 1,
                last_position[value] + 1,
                right,
                change,
            )
            last_position[value] = right

            left = first_zero(1, 0, n - 1, right)
            if left != -1:
                longest = max(longest, right - left + 1)

        return longest
