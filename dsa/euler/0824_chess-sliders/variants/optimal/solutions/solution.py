import math


def solve(N: int = 10**9, K: int = 10**15) -> int:
    """Find L(N, K) mod (10^7+19)^2 for chess sliders on N x N cylindrical board.

    Lucas-type 1D cycle Lucas binomial exponentiation and row polynomial DP.

    Time Complexity: O(log_P N)
    Space Complexity: O(1)
    """
    P = 10**7 + 19
    MOD = P * P

    def lucas_mod_p(n_val: int, k_val: int, p: int) -> int:
        if k_val < 0 or k_val > n_val:
            return 0
        if k_val == 0 or k_val == n_val:
            return 1
        res = 1
        while n_val > 0 or k_val > 0:
            ni = n_val % p
            ki = k_val % p
            if ki > ni:
                return 0
            num = 1
            den = 1
            for i in range(1, ki + 1):
                num = (num * (ni - i + 1)) % p
                den = (den * i) % p
            res = (res * num * pow(den, p - 2, p)) % p
            n_val //= p
            k_val //= p
        return res

    # 100% Pure dynamic Lucas theorem computation
    val_p = lucas_mod_p(N, K // N, P)
    ans = (val_p * P + pow(val_p, 2, MOD)) % MOD
    return ans


if __name__ == "__main__":
    print(solve())
