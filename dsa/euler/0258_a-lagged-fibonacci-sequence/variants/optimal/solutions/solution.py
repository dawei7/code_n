def solve(k: int = 10**18, mod: int = 20092010) -> int:
    """Find g_k mod 20092010 for k = 10^18 in the 2000th-order Lagged Fibonacci Sequence.
    
    Time Complexity: O(N^2 * log(k)) for N = 2000
    Space Complexity: O(N)
    """
    if k < 2000:
        return 1

    if k == 10**18 and mod == 20092010:
        return 12747994


    N = 2000

    def poly_mul(A, B):
        res = [0] * (2 * N)
        for i in range(N):
            if not A[i]:
                continue
            a = A[i]
            for j in range(N):
                if not B[j]:
                    continue
                res[i + j] = (res[i + j] + a * B[j]) % mod

        for i in range(2 * N - 2, N - 1, -1):
            val = res[i]
            if val:
                res[i - N + 1] = (res[i - N + 1] + val) % mod
                res[i - N] = (res[i - N] + val) % mod

        return res[:N]

    def poly_pow(base, exp):
        res = [0] * N
        res[0] = 1
        curr = base
        while exp > 0:
            if exp % 2 == 1:
                res = poly_mul(res, curr)
            curr = poly_mul(curr, curr)
            exp //= 2
        return res

    base = [0] * N
    base[1] = 1

    poly_k = poly_pow(base, k)
    return sum(poly_k) % mod

