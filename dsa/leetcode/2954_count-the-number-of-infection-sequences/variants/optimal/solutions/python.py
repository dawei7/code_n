MOD = 10**9 + 7

def solve(n: int, sick: list[int]) -> int:
    if not sick:
        return 0
    
    # Precompute factorials for combinations
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

    gaps = []
    # Gap before the first sick computer
    gaps.append(sick[0])
    # Gaps between sick computers
    for i in range(len(sick) - 1):
        gaps.append(sick[i + 1] - sick[i] - 1)
    # Gap after the last sick computer
    gaps.append(n - 1 - sick[-1])
    
    total_healthy = n - len(sick)
    ans = fact[total_healthy]
    
    # Divide by the factorial of each gap size (multinomial coefficient)
    for g in gaps:
        ans = (ans * inv[g]) % MOD
        
    # Multiply by 2^(k-1) for each internal gap of size k
    for i in range(1, len(gaps) - 1):
        if gaps[i] > 0:
            ans = (ans * pow(2, gaps[i] - 1, MOD)) % MOD
            
    return ans
