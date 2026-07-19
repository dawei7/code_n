def solve(nums: list[int], k: int) -> int:
    """
    Calculates the X value of the array by analyzing bitwise contributions
    of all subarrays.
    """
    n = len(nums)
    ans = 0
    
    # We process each bit position independently.
    # For each bit, we count how many subarrays have an XOR sum
    # with that bit set.
    for bit in range(31):
        # Current bit contribution
        count_ones = 0
        
        # Prefix XORs for the current bit
        # prefix_xor[i] is the XOR sum of nums[0...i-1]
        # We only care about the 'bit'-th bit.
        current_prefix = 0
        
        # Track counts of prefix XORs seen so far (0 or 1)
        # count[0] is number of prefixes with bit 0, count[1] with bit 1
        counts = [1, 0]
        
        total_subarrays_with_bit = 0
        
        for x in nums:
            # Update prefix XOR for this bit
            if (x >> bit) & 1:
                current_prefix ^= 1
            
            # If current_prefix is 1, we need previous prefix to be 0
            # If current_prefix is 0, we need previous prefix to be 1
            total_subarrays_with_bit += counts[1 - current_prefix]
            
            # Update counts
            counts[current_prefix] += 1
            
        # If the number of subarrays with this bit set satisfies the condition
        # (e.g., divisible by k or similar logic depending on specific problem variant)
        if total_subarrays_with_bit % k == 0:
            ans |= (1 << bit)
            
    return ans
