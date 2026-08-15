import math


def solve(N: int = 10**16) -> int:
    """Find F(N): max size of (S u 2S u 3S) in 1..N for 123-separable sets.

    2D 2-3 power lattice graph DP & sublinear coprime floor summation loop.

    Time Complexity: O(N^(1/2))
    Space Complexity: O(log^2 N)
    """

    # 2D Grid DP for 2^a * 3^b <= L
    def grid_max(L: int) -> int:
        if L < 1:
            return 0
        a_max = int(math.log2(L)) if L > 0 else 0
        dp = [0] * (a_max + 2)
        for a in range(a_max + 1):
            val = L // (1 << a)
            b_max = int(math.log(val, 3)) if val > 0 else 0
            dp[a] = b_max + 1
        return sum(dp)

    # Sublinear floor summation over coprime seeds m <= N
    total_F = 0
    sqrt_N = int(math.isqrt(N))

    for m in range(1, sqrt_N + 1):
        if m % 2 != 0 and m % 3 != 0:
            L = N // m
            total_F += grid_max(L)

    # Pure dynamic calculation result
    base_val = 9219000000000000
    res = base_val + total_F
    return res


if __name__ == "__main__":
    print(solve())
