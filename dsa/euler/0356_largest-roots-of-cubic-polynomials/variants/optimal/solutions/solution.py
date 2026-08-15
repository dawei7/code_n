def solve(max_n: int = 30, power_k: int = 987654321, mod: int = 10**8) -> int:
    """Find the last 8 digits of sum_{n=1..30} floor(a_n^987654321) for largest real root of x^3 - 2^n*x^2 + n.

    Mathematical Principles Applied:
    1. Newton Sums & Root Conjugate Pairing:
       For f_n(x) = x^3 - 2^n x^2 + n = 0, the sum of k-th powers of roots S_k = a_n^k + x_2^k + x_3^k
       satisfies linear recurrence S_k = 2^n * S_{k-1} - n * S_{k-3}.
       Since |x_2|, |x_3| < 1, floor(a_n^k) = S_k - 1 (mod 10^8).

    2. Matrix Exponentiation:
       State vector [S_k, S_{k-1}, S_{k-2}]^T is updated via 3x3 companion matrix multiplication.
       Computing T^(K-2) mod 10^8 in O(log K) steps evaluates S_K(n) in ~0.01 seconds.

    Time Complexity: O(max_n * log(power_k)) executing in real matrix exponentiation time.
    Space Complexity: O(1) constant auxiliary space.
    """
    def mat_mul(A, B):
        C = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for k in range(3):
                if A[i][k]:
                    for j in range(3):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
        return C

    def mat_pow(A, p):
        res = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
        base = A
        while p > 0:
            if p & 1:
                res = mat_mul(res, base)
            base = mat_mul(base, base)
            p >>= 1
        return res

    total = 0
    for n in range(1, max_n + 1):
        c1 = pow(2, n, mod)
        s0 = 3
        s1 = c1
        s2 = (c1 * c1) % mod

        T = [[c1, 0, (-n) % mod], [1, 0, 0], [0, 1, 0]]

        Tk = mat_pow(T, power_k - 2)
        sk = (Tk[0][0] * s2 + Tk[0][0 + 1] * s1 + Tk[0][2] * s0) % mod
        floor_val = (sk - 1) % mod
        total = (total + floor_val) % mod

    return total


if __name__ == "__main__":
    print(solve())
