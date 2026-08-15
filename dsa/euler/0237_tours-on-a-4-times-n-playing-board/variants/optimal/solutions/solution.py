def solve(target_n: int = 10**12, mod: int = 10**8) -> int:
    """Find T(10^12) mod 10^8, the number of Hamiltonian tours on a 4 x N board from (0,0) to (3,0).

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Hamiltonian Grid Paths:
       Let T(n) be the number of paths visiting every square of a 4 x n grid exactly once,
       starting at top-left (0, 0) and ending at bottom-left (3, 0).

    2. Linear Recurrence Relation:
       Transfer matrix column connectivity analysis yields the 4th-order linear recurrence:
           T(n) = 2*T(n-1) + 2*T(n-2) - 2*T(n-3) + T(n-4)   for n >= 5,
       with initial terms:
           T(1) = 1, T(2) = 1, T(3) = 4, T(4) = 8.

    3. Matrix Exponentiation:
       In state vector form:
           [T(n), T(n-1), T(n-2), T(n-3)]^T = M^(n-4) * [T(4), T(3), T(2), T(1)]^T
       where M is the 4x4 companion matrix:
           M = [[ 2,  2, -2,  1],
                [ 1,  0,  0,  0],
                [ 0,  1,  0,  0],
                [ 0,  0,  1,  0]].

    Complexity:
    -----------
    - Time Complexity: O(k^3 * log(n)) where k = 4, n = 10^12 (< 0.001 seconds).
    - Space Complexity: O(k^2) matrix storage (~1 KB).
    """
    MOD = mod
    M = [[2, 2, -2, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]

    def mat_mul(
        A: list[list[int]], B: list[list[int]], size: int = 4
    ) -> list[list[int]]:
        C = [[0] * size for _ in range(size)]
        for i in range(size):
            for k in range(size):
                if A[i][k] == 0:
                    continue
                for j in range(size):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
        return C

    def mat_pow(A: list[list[int]], p: int, size: int = 4) -> list[list[int]]:
        res = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
        base = A
        while p > 0:
            if p % 2 == 1:
                res = mat_mul(res, base, size)
            base = mat_mul(base, base, size)
            p //= 2
        return res

    if target_n <= 4:
        initial_terms = [0, 1, 1, 4, 8]
        return initial_terms[target_n] % MOD

    M_pow = mat_pow(M, target_n - 4)
    v = [8, 4, 1, 1]
    ans = sum(M_pow[0][j] * v[j] for j in range(4)) % MOD
    return ans


if __name__ == "__main__":
    print(solve())
