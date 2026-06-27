def solve(nums1: list[int], nums2: list[int]) -> int:
    n = len(nums1)
    
    def count_swaps(last1, last2):
        swaps = 0
        for i in range(n):
            a, b = nums1[i], nums2[i]
            # If current elements already satisfy the condition
            if a <= last1 and b <= last2:
                continue
            # Try swapping to satisfy the condition
            elif b <= last1 and a <= last2:
                swaps += 1
            else:
                # Impossible to satisfy
                return float('inf')
        return swaps

    # Scenario 1: Keep the last elements as they are
    res1 = count_swaps(nums1[-1], nums2[-1])
    
    # Scenario 2: Swap the last elements
    res2 = count_swaps(nums2[-1], nums1[-1]) + 1
    
    ans = min(res1, res2)
    return int(ans) if ans != float('inf') else -1
