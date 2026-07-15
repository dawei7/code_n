from collections import Counter
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        heap = [
            (-count, value)
            for value, count in Counter(barcodes).items()
        ]
        heapify(heap)

        result = []
        previous_count = 0
        previous_value = 0

        while heap:
            count, value = heappop(heap)
            result.append(value)

            if previous_count < 0:
                heappush(heap, (previous_count, previous_value))

            previous_count = count + 1
            previous_value = value

        return result

