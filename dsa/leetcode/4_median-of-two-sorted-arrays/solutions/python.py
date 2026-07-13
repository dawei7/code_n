def solve(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    total = len(nums1) + len(nums2)
    left_size = (total + 1) // 2
    low, high = 0, len(nums1)

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = left_size - cut1
        left1 = nums1[cut1 - 1] if cut1 else float("-inf")
        right1 = nums1[cut1] if cut1 < len(nums1) else float("inf")
        left2 = nums2[cut2 - 1] if cut2 else float("-inf")
        right2 = nums2[cut2] if cut2 < len(nums2) else float("inf")

        if left1 <= right2 and left2 <= right1:
            if total % 2:
                return float(max(left1, left2))
            return (max(left1, left2) + min(right1, right2)) / 2.0
        if left1 > right2:
            high = cut1 - 1
        else:
            low = cut1 + 1

    raise ValueError("inputs must be sorted and at least one must be non-empty")
