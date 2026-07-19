from bisect import bisect_left, bisect_right


def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    def count_at_most(limit: int) -> int:
        count = 0

        for first in nums1:
            if first > 0:
                count += bisect_right(nums2, limit // first)
            elif first == 0:
                if limit >= 0:
                    count += len(nums2)
            else:
                threshold = -((-limit) // first)
                count += len(nums2) - bisect_left(nums2, threshold)

        return count

    low = -(10**10)
    high = 10**10

    while low < high:
        middle = (low + high) // 2
        if count_at_most(middle) >= k:
            high = middle
        else:
            low = middle + 1

    return low
