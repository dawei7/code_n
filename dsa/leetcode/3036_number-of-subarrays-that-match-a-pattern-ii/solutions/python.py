def solve(nums: list[int], pattern: list[int]) -> int:
    n = len(nums)
    m = len(pattern)
    
    # Transform nums into a sequence of relations
    # relations[i] represents the relationship between nums[i] and nums[i+1]
    relations = []
    for i in range(n - 1):
        if nums[i+1] > nums[i]:
            relations.append(1)
        elif nums[i+1] == nums[i]:
            relations.append(0)
        else:
            relations.append(-1)
            
    # KMP Algorithm: Precompute the failure function (pi table) for the pattern
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
        
    # KMP Algorithm: Search for pattern in relations
    count = 0
    j = 0
    for i in range(len(relations)):
        while j > 0 and relations[i] != pattern[j]:
            j = pi[j - 1]
        if relations[i] == pattern[j]:
            j += 1
        if j == m:
            count += 1
            j = pi[j - 1]
            
    return count
