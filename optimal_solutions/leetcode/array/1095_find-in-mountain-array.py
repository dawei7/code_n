"""Optimal solution for LeetCode 1095: Find in Mountain Array."""

from typing import Protocol


class MountainArray(Protocol):
    def get(self, index: int) -> int: ...
    def length(self) -> int: ...


def solve(target: int, mountain_arr: MountainArray) -> int:
    n = mountain_arr.length()
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
            left = mid + 1
        else:
            right = mid
    peak = left

    def search(lo: int, hi: int, ascending: bool) -> int:
        while lo <= hi:
            mid = (lo + hi) // 2
            value = mountain_arr.get(mid)
            if value == target:
                return mid
            if (value < target) == ascending:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    answer = search(0, peak, True)
    return answer if answer != -1 else search(peak + 1, n - 1, False)
