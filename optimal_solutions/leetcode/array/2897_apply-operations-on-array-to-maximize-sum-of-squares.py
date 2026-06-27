def solve(nums: list[int], k: int) -> int:
    MOD = 10**9 + 7
    
    # Count the frequency of each bit position (0 to 31)
    bit_counts = [0] * 32
    for x in nums:
        for i in range(32):
            if (x >> i) & 1:
                bit_counts[i] += 1
                
    # Construct k numbers by greedily assigning bits from highest to lowest
    # To maximize sum of squares, we want to make the largest numbers as large as possible
    result_nums = [0] * k
    for i in range(31, -1, -1):
        # Distribute the available bits at position i to the first few numbers
        count = bit_counts[i]
        for j in range(min(count, k)):
            result_nums[j] |= (1 << i)
            
    # Calculate the sum of squares modulo 10^9 + 7
    total_sum = 0
    for x in result_nums:
        total_sum = (total_sum + (x * x)) % MOD
        
    return total_sum
