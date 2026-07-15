# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class MountainArray:
#     def get(self, index: int) -> int:
#     def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        def binary_search(low: int, high: int, ascending: bool) -> int:
            while low <= high:
                mid = (low + high) // 2
                value = mountainArr.get(mid)
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
        return binary_search(peak + 1, length - 1, False)
