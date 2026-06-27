def solve(nums):
    MOD = 10**9 + 7
    count0 = 0
    count1 = 0
    count2 = 0

    for num in nums:
        if num == 0:
            # A new subsequence ending in 0 can be formed by:
            # 1. Appending this 0 to existing subsequences ending in 0 (count0 ways).
            # 2. Starting a new subsequence with this 0 (1 way).
            # Total new subsequences ending in 0 = count0 (existing) + count0 (append) + 1 (new single 0)
            # This simplifies to 2 * count0 + 1
            count0 = (2 * count0 + 1) % MOD
        elif num == 1:
            # A new subsequence ending in 1 can be formed by:
            # 1. Appending this 1 to existing subsequences ending in 0 (count0 ways).
            # 2. Appending this 1 to existing subsequences ending in 1 (count1 ways).
            # Total new subsequences ending in 1 = count1 (existing) + count0 (append to 0s) + count1 (append to 1s)
            # This simplifies to count0 + 2 * count1
            count1 = (count0 + 2 * count1) % MOD
        elif num == 2:
            # A new subsequence ending in 2 can be formed by:
            # 1. Appending this 2 to existing subsequences ending in 1 (count1 ways).
            # 2. Appending this 2 to existing subsequences ending in 2 (count2 ways).
            # Total new subsequences ending in 2 = count2 (existing) + count1 (append to 1s) + count2 (append to 2s)
            # This simplifies to count1 + 2 * count2
            count2 = (count1 + 2 * count2) % MOD

    # The final answer is the total count of special subsequences ending in 2.
    return count2
