MOD = 10**9 + 7

def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    nums.sort()
    
    fact = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD
        
    inv[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD
        
    def nCr(n, r):
        if r < 0 or r > n:
            return 0
        num = fact[n]
        den = (inv[r] * inv[n - r]) % MOD
        return (num * den) % MOD

    # Precompute sum of combinations: sum_{i=0}^{k-1} nCr(m, i)
    # This represents choosing up to k-1 other elements
    comb_sum = [0] * (n + 1)
    current_sum = 0
    for i in range(n + 1):
        current_sum = (current_sum + nCr(n - 1, i)) % MOD
        comb_sum[i] = current_sum
        
    # To get sum of nCr(m, j) for j from 0 to k-1:
    def get_comb_sum(m, k_limit):
        if k_limit <= 0: return 0
        # We need sum_{j=0}^{k-1} nCr(m, j)
        # If k-1 >= m, sum is 2^m. Otherwise use precomputed or direct
        if k_limit - 1 >= m:
            return pow(2, m, MOD)
        res = 0
        for j in range(min(k_limit, m + 1)):
            res = (res + nCr(m, j)) % MOD
        return res

    total_sum = 0
    for i in range(n):
        # nums[i] as min: elements to the right are n-1-i
        # We choose some number of elements from the right (0 to k-1)
        count_min = get_comb_sum(n - 1 - i, k - 1)
        
        # nums[i] as max: elements to the left are i
        # We choose some number of elements from the left (0 to k-1)
        count_max = get_comb_sum(i, k - 1)
        
        total_sum = (total_sum + nums[i] * count_min) % MOD
        total_sum = (total_sum + nums[i] * count_max) % MOD
        
    return total_sum
