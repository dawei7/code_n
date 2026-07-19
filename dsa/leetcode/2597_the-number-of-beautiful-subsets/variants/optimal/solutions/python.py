from collections import Counter, defaultdict

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of beautiful subsets using a combinatorial approach.
    We group numbers by their remainder modulo k. Within each group, 
    elements can only conflict if they are adjacent in the sorted sequence 
    of that group (since they differ by exactly k).
    """
    # Count frequencies of each number
    counts = Counter(nums)
    
    # Group numbers by their remainder modulo k
    groups = defaultdict(list)
    for x in counts:
        groups[x % k].append(x)
    
    total_subsets = 1
    
    for rem in groups:
        # Sort numbers in the group to handle the difference k constraint
        group = sorted(groups[rem])
        
        # dp[i] stores the number of ways to form a subset using the first i elements
        # of the group such that no two elements have a difference of k.
        # If we don't include group[i]: ways = dp[i-1]
        # If we include group[i]: we can include it 2^count[group[i]] - 1 times.
        # If group[i] - group[i-1] == k, we cannot include group[i-1].
        
        n = len(group)
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            val = group[i-1]
            take = (pow(2, counts[val]) - 1)
            
            if i > 1 and group[i-1] - group[i-2] == k:
                # Cannot pick both group[i-1] and group[i-2]
                dp[i] = dp[i-1] + dp[i-2] * take
            else:
                # Can pick group[i-1] freely with any valid subset of previous
                dp[i] = dp[i-1] * (take + 1)
        
        total_subsets *= dp[n]
        
    # Subtract 1 to exclude the empty subset
    return total_subsets - 1
