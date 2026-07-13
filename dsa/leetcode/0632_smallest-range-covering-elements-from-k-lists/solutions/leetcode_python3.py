from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(values[0], list_index, 0) for list_index, values in enumerate(nums)]
        heapify(heap)
        current_maximum = max(value for value, _, _ in heap)
        best_left, best_right = heap[0][0], current_maximum

        while True:
            current_minimum, list_index, value_index = heappop(heap)
            current_width = current_maximum - current_minimum
            best_width = best_right - best_left
            if current_width < best_width or (
                current_width == best_width and current_minimum < best_left
            ):
                best_left, best_right = current_minimum, current_maximum

            value_index += 1
            if value_index == len(nums[list_index]):
                return [best_left, best_right]

            next_value = nums[list_index][value_index]
            current_maximum = max(current_maximum, next_value)
            heappush(heap, (next_value, list_index, value_index))
