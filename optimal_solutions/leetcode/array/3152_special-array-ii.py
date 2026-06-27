def solve(nums: list[int], queries: list[list[int]]) -> list[bool]:
    n = len(nums)
    if n == 0:
        return []
    
    # violation[i] is 1 if nums[i] and nums[i+1] have the same parity
    # We only care about indices up to n-2
    violations = [0] * (n - 1)
    for i in range(n - 1):
        if (nums[i] % 2) == (nums[i + 1] % 2):
            violations[i] = 1
            
    # Build prefix sum of violations
    # prefix_sum[i] stores the number of violations in nums[0...i]
    prefix_sum = [0] * n
    for i in range(n - 1):
        prefix_sum[i + 1] = prefix_sum[i] + violations[i]
        
    results = []
    for start, end in queries:
        if start == end:
            results.append(True)
        else:
            # Check if there is any violation in the range [start, end-1]
            # The number of violations in range [start, end-1] is:
            # prefix_sum[end-1] - prefix_sum[start]
            count = prefix_sum[end] - prefix_sum[start]
            results.append(count == 0)
            
    return results
