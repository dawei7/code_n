def solve(s: str, queries: list[list[int]]) -> list[list[int]]:
    # The target value for a query [first, second] is val = first ^ second.
    # Since second <= 10^9, val <= 2^30. We only care about substrings of length <= 30.
    
    val_to_indices = {}
    n = len(s)
    
    # Precompute all possible substring values of length up to 30
    for i in range(n):
        val = 0
        # Limit length to 30 to keep within integer bounds and problem constraints
        for j in range(i, min(i + 30, n)):
            val = (val << 1) | (ord(s[j]) - ord('0'))
            
            # If we haven't seen this value, store the first occurrence
            if val not in val_to_indices:
                val_to_indices[val] = [i, j]
            
            # Optimization: if we encounter a '0', the value doesn't change 
            # but the length increases. We only care about the shortest, 
            # so we don't update if already present.
            if s[i] == '0':
                break
                
    results = []
    for first, second in queries:
        target = first ^ second
        if target in val_to_indices:
            results.append(val_to_indices[target])
        else:
            results.append([-1, -1])
            
    return results
