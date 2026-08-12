def solve(limit: int = 10**17) -> int:
    """Find sum(z(n)) for 0 < n < 10^17 in Zeckendorf representation.
    
    Time Complexity: O(log_phi(limit)) via Memoized Fibonacci Divide and Conquer
    Space Complexity: O(log_phi(limit))
    """
    fibs = [1, 2]
    while fibs[-1] < limit:
        fibs.append(fibs[-1] + fibs[-2])

    memo = {}

    def S_memo(N):
        if N <= 1:
            return 0
        if N in memo:
            return memo[N]
        for f in reversed(fibs):
            if f < N:
                res = S_memo(f) + (N - f) + S_memo(N - f)
                memo[N] = res
                return res

    return S_memo(limit)
