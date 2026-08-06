"""Bounded-space dual-heap solution for LeetCode 480."""

from collections import Counter
from heapq import heapify, heappop, heappush


def solve(nums: list[int], k: int) -> list[float]:
    small: list[int] = []
    large: list[int] = []
    delayed: Counter[int] = Counter()
    small_size = large_size = 0

    def prune(heap: list[int], lower: bool) -> None:
        while heap:
            value = -heap[0] if lower else heap[0]
            pending = delayed.get(value, 0)
            if pending == 0:
                return
            heappop(heap)
            if pending == 1:
                del delayed[value]
            else:
                delayed[value] = pending - 1

    def balance() -> None:
        nonlocal small_size, large_size
        while small_size > large_size + 1:
            heappush(large, -heappop(small))
            small_size -= 1
            large_size += 1
            prune(small, True)
        while small_size < large_size:
            heappush(small, -heappop(large))
            small_size += 1
            large_size -= 1
            prune(large, False)

    def insert(value: int) -> None:
        nonlocal small_size, large_size
        if not small or value <= -small[0]:
            heappush(small, -value)
            small_size += 1
        else:
            heappush(large, value)
            large_size += 1
        balance()

    def erase(value: int) -> None:
        nonlocal small_size, large_size
        delayed[value] += 1
        if value <= -small[0]:
            small_size -= 1
            if value == -small[0]:
                prune(small, True)
        else:
            large_size -= 1
            if value == large[0]:
                prune(large, False)
        balance()

    def compact() -> None:
        nonlocal small, large, small_size, large_size
        if len(small) + len(large) <= 2 * k:
            return

        pending = delayed.copy()

        def retain_valid(heap: list[int], lower: bool) -> list[int]:
            retained: list[int] = []
            for stored in heap:
                value = -stored if lower else stored
                count = pending.get(value, 0)
                if count == 0:
                    retained.append(stored)
                elif count == 1:
                    del pending[value]
                else:
                    pending[value] = count - 1
            return retained

        small = retain_valid(small, True)
        large = retain_valid(large, False)
        heapify(small)
        heapify(large)
        delayed.clear()
        small_size = len(small)
        large_size = len(large)
        balance()

    def median() -> float:
        if k % 2:
            return float(-small[0])
        return (-small[0] + large[0]) / 2.0

    for value in nums[:k]:
        insert(value)

    answer = [median()]
    for index in range(k, len(nums)):
        insert(nums[index])
        erase(nums[index - k])
        compact()
        answer.append(median())
    return answer
