import heapq
from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        maximum_sum = sum(value for value in nums if value > 0)
        losses = sorted(abs(value) for value in nums)

        if k == 1:
            return maximum_sum

        heap = [(losses[0], 0)]
        current_loss = 0

        for _ in range(k - 1):
            current_loss, index = heapq.heappop(heap)
            if index + 1 < len(losses):
                next_loss = losses[index + 1]
                heapq.heappush(
                    heap,
                    (current_loss + next_loss, index + 1),
                )
                heapq.heappush(
                    heap,
                    (
                        current_loss - losses[index] + next_loss,
                        index + 1,
                    ),
                )

        return maximum_sum - current_loss
