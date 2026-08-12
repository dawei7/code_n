def solve(target_n: int = 10**12, mod: int = 10**8) -> int:
    """Find T(10^12) mod 10^8, the number of Hamiltonian tours on a 4 x N board from (0,0) to (3,0).
    
    Time Complexity: O(order^3 * log(target_n)) for 4x4 matrix exponentiation
    Space Complexity: O(order^2)
    """
    MOD = mod
    M = [[2, 2, -2, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]

    def mat_mul(A, B):
        size = len(A)
        C = [[0] * size for _ in range(size)]
        for i in range(size):
            for k in range(size):
                if A[i][k] == 0:
                    continue
                for j in range(size):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
        return C

    def mat_pow(A, p):
        size = len(A)
        res = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
        base = A
        while p > 0:
            if p % 2 == 1:
                res = mat_mul(res, base)
            base = mat_mul(base, base)
            p //= 2
        return res

    M_pow = mat_pow(M, target_n - 4)
    v = [8, 4, 1, 1]
    ans = sum(M_pow[0][j] * v[j] for j in range(4)) % MOD
    return ans
