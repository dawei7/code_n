from collections import Counter
from heapq import heappop, heappush
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small, large = [], []
        delayed = Counter()
        small_size = large_size = 0

        def prune(heap, lower):
            while heap:
                value = -heap[0] if lower else heap[0]
                if delayed[value] == 0:
                    break
                heappop(heap)
                delayed[value] -= 1

        def balance():
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                heappush(large, -heappop(small))
                small_size -= 1
                large_size += 1
                prune(small, True)
            elif small_size < large_size:
                heappush(small, -heappop(large))
                small_size += 1
                large_size -= 1
                prune(large, False)

        def insert(value):
            nonlocal small_size, large_size
            if not small or value <= -small[0]:
                heappush(small, -value)
                small_size += 1
            else:
                heappush(large, value)
                large_size += 1
            balance()

        def erase(value):
            nonlocal small_size, large_size
            delayed[value] += 1
            if value <= -small[0]:
                small_size -= 1
                if value == -small[0]:
                    prune(small, True)
            else:
                large_size -= 1
                if large and value == large[0]:
                    prune(large, False)
            balance()

        def median():
            return float(-small[0]) if k % 2 else (-small[0] + large[0]) / 2.0

        for value in nums[:k]:
            insert(value)
        answer = [median()]
        for index in range(k, len(nums)):
            insert(nums[index])
            erase(nums[index - k])
            answer.append(median())
        return answer
