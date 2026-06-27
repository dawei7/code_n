def solve(nums: list[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0
    
    # Precompute LCP table
    # lcp[i][j] is the length of the longest common prefix of nums[i:] and nums[j:]
    lcp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if nums[i] == nums[j]:
                lcp[i][j] = 1 + lcp[i + 1][j + 1]
            else:
                lcp[i][j] = 0
                
    count = 0
    # Split into three parts: [0, i-1], [i, j-1], [j, n-1]
    # 0 < i < j < n
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            len1 = i
            len2 = j - i
            len3 = n - j
            
            # Condition 1: nums1 is prefix of nums2
            # nums1 starts at 0, nums2 starts at i
            # Check if len1 <= len2 and lcp[0][i] >= len1
            cond1 = (len1 <= len2 and lcp[0][i] >= len1)
            
            # Condition 2: nums2 is prefix of nums3
            # nums2 starts at i, nums3 starts at j
            # Check if len2 <= len3 and lcp[i][j] >= len2
            cond2 = (len2 <= len3 and lcp[i][j] >= len2)
            
            if cond1 or cond2:
                count += 1
                
    return count
