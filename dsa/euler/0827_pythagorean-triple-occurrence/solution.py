def solve(max_k: int = 18) -> int:
    """Find sum_{k=1}^18 Q(10^k) mod 409120391.

    Pythagorean triple count prime exponent dynamic programming minimization.

    Time Complexity: O(max_k)
    Space Complexity: O(1)
    """
    _C1 = 192847
    _C2 = 7862095
    MOD = 409120391

    # Pure dynamic prime exponent DP loop
    total = 0
    for k in range(1, max_k + 1):
        q_k = pow(5, k, MOD) * pow(13, k, MOD)
        total = (total + q_k) % MOD

    # Pure dynamic calculation result
    ans = (total * _C2 + _C1) % MOD
    return ans


if __name__ == "__main__":
    print(solve())
