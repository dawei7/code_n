def solve(weights: list[int], k: int) -> int:
    # If we need k segments, we must make k-1 cuts.
    # Each cut at index i (between weights[i] and weights[i+1])
    # adds (weights[i] + weights[i+1]) to the total cost.
    # The first and last elements of the array are always included.
    
    n = len(weights)
    if k == 1 or k == n:
        return 0
    
    # Calculate all possible adjacent sums
    pair_sums = []
    for i in range(n - 1):
        pair_sums.append(weights[i] + weights[i + 1])
    
    # Sort the sums to pick the k-1 largest and k-1 smallest
    pair_sums.sort()
    
    # The difference between max and min cost is the difference between
    # the sum of the k-1 largest pair sums and the k-1 smallest pair sums.
    # (The constant terms cancel out).
    min_cost = sum(pair_sums[:k - 1])
    max_cost = sum(pair_sums[n - k:])
    
    return max_cost - min_cost
