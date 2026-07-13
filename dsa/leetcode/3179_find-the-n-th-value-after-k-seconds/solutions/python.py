def solve(n: int, k: int) -> int:
    """
    Calculates the value at index n-1 after k seconds.
    The value at index i after k seconds is C(i + k, i).
    For index n-1, this is C(n - 1 + k, n - 1) = C(n + k - 1, k).
    """
    MOD = 10**9 + 7
    
    # We need to calculate C(n + k - 1, k)
    # C(N, K) = N! / (K! * (N-K)!)
    # Here N = n + k - 1, K = k
    # C(n + k - 1, k) = [(n+k-1) * (n+k-2) * ... * (n)] / k!
    
    N = n + k - 1
    K = min(k, n - 1)
    
    if K < 0:
        return 0
    if K == 0:
        return 1
        
    # Calculate C(N, K)
    numerator = 1
    denominator = 1
    for i in range(K):
        numerator = (numerator * (N - i)) % MOD
        denominator = (denominator * (i + 1)) % MOD
        
    # Modular inverse using Fermat's Little Theorem
    return (numerator * pow(denominator, MOD - 2, MOD)) % MOD
