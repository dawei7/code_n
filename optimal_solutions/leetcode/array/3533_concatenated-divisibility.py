def solve(nums: list[int], k: int) -> bool:
    n = len(nums)
    # Precompute lengths and powers of 10 mod k
    str_nums = [str(x) for x in nums]
    lengths = [len(s) for s in str_nums]
    remainders = [int(s) % k for s in str_nums]
    
    # powers[i][j] = 10^lengths[j] % k
    powers = [[0] * n for _ in range(n)]
    for i in range(n):
        p = pow(10, lengths[i], k)
        for j in range(n):
            powers[j][i] = p
            
    # dp[mask] stores a set of possible remainders modulo k
    # using the subset of numbers represented by the bitmask
    dp = [set() for _ in range(1 << n)]
    
    for i in range(n):
        dp[1 << i].add(remainders[i])
        
    for mask in range(1, 1 << n):
        if not dp[mask]:
            continue
            
        # Try adding a new number j not in mask
        for j in range(n):
            if not (mask & (1 << j)):
                new_mask = mask | (1 << j)
                p_j = powers[j][mask] # 10^len(mask) % k
                # The new remainder is (current_remainder * 10^len(j) + remainder_j) % k
                # Wait, the order is: (existing_number * 10^len(new) + new_number) % k
                # So we need 10^len(new) % k
                
                # Correct logic:
                # If we append nums[j] to the end of the existing concatenation:
                # new_rem = (old_rem * 10^len(nums[j]) + nums[j]) % k
                
                shift = pow(10, lengths[j], k)
                for rem in dp[mask]:
                    new_rem = (rem * shift + remainders[j]) % k
                    dp[new_mask].add(new_rem)
                    
    for mask in range(1, 1 << n):
        if 0 in dp[mask]:
            return True
            
    return False
