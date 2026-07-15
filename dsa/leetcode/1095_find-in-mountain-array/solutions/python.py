"""Optimal app-local solution for LeetCode 1095."""


def solve(target: int, mountain_arr: list[int]) -> int:
    left, right = 0, len(mountain_arr) - 1
    while left < right:
        mid = (left + right) // 2
        if mountain_arr[mid] < mountain_arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    peak = left

    def binary_search(low: int, high: int, ascending: bool) -> int:
        while low <= high:
            mid = (low + high) // 2
            value = mountain_arr[mid]
            if value == target:
                return mid
            if (value < target) == ascending:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    answer = binary_search(0, peak, True)
    if answer != -1:
        return answer
    return binary_search(peak + 1, len(mountain_arr) - 1, False)
