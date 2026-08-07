from collections import Counter
from heapq import heappop, heappush
from typing import List


class Solution:
    def modeWeight(self, nums: List[int], k: int) -> int:
        frequency = Counter()
        candidates = []

        def add(value: int) -> None:
            frequency[value] += 1
            heappush(candidates, (-frequency[value], value))

        def remove(value: int) -> None:
            frequency[value] -= 1
            if frequency[value] > 0:
                heappush(candidates, (-frequency[value], value))

        def weight() -> int:
            while -candidates[0][0] != frequency[candidates[0][1]]:
                heappop(candidates)
            count, value = candidates[0]
            return -count * value

        for value in nums[:k]:
            add(value)

        answer = weight()
        for right in range(k, len(nums)):
            remove(nums[right - k])
            add(nums[right])
            answer += weight()

        return answer
