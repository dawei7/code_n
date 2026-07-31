def solve(nums1: list[int], nums2: list[int]) -> int:
    a = sorted(nums1)
    b = sorted(nums2)

    for start in range(2, -1, -1):
        x = b[0] - a[start]
        j = 0
        for value in a:
            if j < len(b) and value + x == b[j]:
                j += 1
        if j == len(b):
            return x
