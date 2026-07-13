"""Optimal solution for LeetCode 1095: Find in Mountain Array."""


def solve(target: int, mountain_arr) -> int:
    def get(index: int) -> int:
        if isinstance(mountain_arr, list):
            return mountain_arr[index]
        return mountain_arr.get(index)

    def length() -> int:
        if isinstance(mountain_arr, list):
            return len(mountain_arr)
        return mountain_arr.length()

    n = length()
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if get(mid) < get(mid + 1):
            left = mid + 1
        else:
            right = mid
    peak = left

    def search(lo: int, hi: int, ascending: bool) -> int:
        while lo <= hi:
            mid = (lo + hi) // 2
            value = get(mid)
            if value == target:
                return mid
            if (value < target) == ascending:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    answer = search(0, peak, True)
    return answer if answer != -1 else search(peak + 1, n - 1, False)
