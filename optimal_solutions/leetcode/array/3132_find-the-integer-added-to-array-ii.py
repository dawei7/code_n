def solve(nums1: list[int], nums2: list[int]) -> int:
    nums1.sort()
    nums2.sort()
    n = len(nums1)
    m = len(nums2)
    
    def check(diff: int) -> bool:
        # Try to match nums2 using two pointers on nums1
        # We are allowed to skip exactly 2 elements in nums1
        p1 = 0
        p2 = 0
        skips = 0
        while p1 < n and p2 < m:
            if nums1[p1] + diff == nums2[p2]:
                p1 += 1
                p2 += 1
            else:
                skips += 1
                p1 += 1
                if skips > 2:
                    return False
        return p2 == m

    # The possible difference must be formed by nums2[0] - nums1[i]
    # where i is one of the first 3 elements (because we only remove 2)
    candidates = set()
    for i in range(3):
        candidates.add(nums2[0] - nums1[i])
    
    # Sort candidates to find the smallest valid one
    for diff in sorted(list(candidates)):
        if check(diff):
            return diff
            
    return 0
