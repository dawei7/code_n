def solve(nums, queries):
    """
    Computes range sums for an immutable array using prefix sums.
    
    Args:
        nums: List[int] - The input array.
        queries: List[List[int]] - A list of [left, right] ranges.
        
    Returns:
        List[int] - The results of the range sum queries.
    """
    if not nums:
        return []
    
    # Pre-compute prefix sums
    # prefix_sums[i] stores the sum of nums[0...i-1]
    n = len(nums)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
    results = []
    for left, right in queries:
        # The sum of range [left, right] is prefix_sums[right + 1] - prefix_sums[left]
        range_sum = prefix_sums[right + 1] - prefix_sums[left]
        results.append(range_sum)
        
    return results
