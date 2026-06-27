from collections import Counter

def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    # Precompute bitmasks for numbers 1-30
    # A number is invalid if it's divisible by a square (4, 9, 25)
    masks = {}
    for i in range(1, 31):
        temp = i
        mask = 0
        is_square_free = True
        for idx, p in enumerate(primes):
            count = 0
            while temp % p == 0:
                count += 1
                temp //= p
            if count > 1:
                is_square_free = False
                break
            if count == 1:
                mask |= (1 << idx)
        if is_square_free:
            masks[i] = mask
            
    counts = Counter(nums)
    # dp[mask] stores the number of ways to get a product with prime factors represented by mask
    dp = {0: 1}
    
    for num, freq in counts.items():
        if num not in masks:
            continue
        
        num_mask = masks[num]
        new_dp = dp.copy()
        
        for mask, count in dp.items():
            if (mask & num_mask) == 0:
                new_mask = mask | num_mask
                # If num is 1, it can be included in any existing subset
                # If num > 1, we multiply by freq
                ways = (count * freq) % MOD
                new_dp[new_mask] = (new_dp.get(new_mask, 0) + ways) % MOD
        dp = new_dp
        
    # Subtract 1 to exclude the empty subset
    return (dp.get(0, 1) - 1 + sum(dp.values()) - dp.get(0, 1)) % MOD
