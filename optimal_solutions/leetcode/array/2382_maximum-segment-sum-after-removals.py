def solve(nums: list[int], removeQueries: list[int]) -> list[int]:
    n = len(nums)
    parent = list(range(n))
    sums = [0] * n
    exists = [False] * n
    ans = [0] * n
    
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]
    
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            sums[root_j] += sums[root_i]
            
    current_max = 0
    results = []
    
    # Process in reverse: adding elements back
    for i in reversed(range(n)):
        results.append(current_max)
        idx = removeQueries[i]
        exists[idx] = True
        sums[idx] = nums[idx]
        
        # Check left neighbor
        if idx > 0 and exists[idx - 1]:
            union(idx, idx - 1)
        # Check right neighbor
        if idx < n - 1 and exists[idx + 1]:
            union(idx, idx + 1)
            
        current_max = max(current_max, sums[find(idx)])
        
    return results[::-1]
