def solve(nums: list[int], pattern: list[int]) -> int:
    n = len(nums)
    m = len(pattern)
    
    # Transform nums into a relationship sequence
    # rels[i] represents the relationship between nums[i] and nums[i+1]
    rels = []
    for i in range(n - 1):
        if nums[i+1] > nums[i]:
            rels.append(1)
        elif nums[i+1] == nums[i]:
            rels.append(0)
        else:
            rels.append(-1)
            
    count = 0
    # We need to find how many subarrays of length m in rels match pattern
    # The number of possible starting positions is len(rels) - m + 1
    if len(rels) < m:
        return 0
        
    for i in range(len(rels) - m + 1):
        match = True
        for j in range(m):
            if rels[i + j] != pattern[j]:
                match = False
                break
        if match:
            count += 1
            
    return count
