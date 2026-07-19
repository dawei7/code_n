def solve(nums: list[int]) -> int:
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] ^ nums[i]
    
    count = 0
    # We need to find triplets (i, j, k) such that 0 <= i < j <= k < n
    # Condition: XOR(i, j-1) == XOR(j, k)
    # This is equivalent to: (prefix[j] ^ prefix[i]) == (prefix[k+1] ^ prefix[j])
    # Which simplifies to: prefix[i] == prefix[k+1]
    
    # Iterate over all possible i and k such that i < k
    # For a fixed i and k, any j such that i < j <= k is valid.
    # The number of such j values is (k - i).
    for i in range(n):
        for k in range(i + 1, n):
            if prefix[i] == prefix[k + 1]:
                count += (k - i)
                
    return count
