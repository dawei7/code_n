import heapq
from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0

        values = nums[:]
        previous = [index - 1 for index in range(size)]
        following = [index + 1 for index in range(size)]
        following[-1] = -1
        active = [True] * size

        heap = [
            (values[index] + values[index + 1], index, index + 1)
            for index in range(size - 1)
        ]
        heapq.heapify(heap)
        inversions = sum(
            values[index] > values[index + 1] for index in range(size - 1)
        )

        operations = 0
        while inversions:
            while True:
                pair_sum, left, right = heapq.heappop(heap)
                if (
                    active[left]
                    and active[right]
                    and following[left] == right
                    and values[left] + values[right] == pair_sum
                ):
                    break

            before = previous[left]
            after = following[right]

            if before != -1:
                inversions -= values[before] > values[left]
            inversions -= values[left] > values[right]
            if after != -1:
                inversions -= values[right] > values[after]

            values[left] = pair_sum
            active[right] = False
            following[left] = after
            if after != -1:
                previous[after] = left

            if before != -1:
                inversions += values[before] > values[left]
                heapq.heappush(
                    heap, (values[before] + values[left], before, left)
                )
            if after != -1:
                inversions += values[left] > values[after]
                heapq.heappush(heap, (values[left] + values[after], left, after))

            operations += 1

        return operations
