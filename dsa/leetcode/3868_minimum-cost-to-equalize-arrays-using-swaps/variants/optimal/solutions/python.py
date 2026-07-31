from collections import Counter


def solve(nums1: list[int], nums2: list[int]) -> int:
    count1 = Counter(nums1)
    count2 = Counter(nums2)

    mismatch_count = 0
    for value in count1.keys() | count2.keys():
        if (count1[value] + count2[value]) % 2:
            return -1
        mismatch_count += abs(count1[value] - count2[value])

    return mismatch_count // 4
