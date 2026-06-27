def solve(nums: list[int], threshold: int) -> int:
    parent = list(range(threshold + 1))
    
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
            
    exists = [False] * (threshold + 1)
    for x in nums:
        if x <= threshold:
            exists[x] = True
            
    # For every possible GCD 'g', if we have multiples 'a' and 'b' 
    # such that (a * b) / g <= threshold, they are connected.
    # This is equivalent to connecting multiples of g to g itself 
    # if the multiple is <= threshold.
    for g in range(1, threshold + 1):
        first_multiple = -1
        for multiple in range(g, threshold + 1, g):
            if exists[multiple]:
                if first_multiple == -1:
                    first_multiple = multiple
                else:
                    # If lcm(first, multiple) = (first * multiple) / g <= threshold
                    if (first_multiple * multiple) // g <= threshold:
                        union(first_multiple, multiple)
    
    # Count unique components for numbers present in nums
    unique_roots = set()
    count = 0
    for x in nums:
        root = find(x)
        if root not in unique_roots:
            unique_roots.add(root)
            count += 1
            
    return count
