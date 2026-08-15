MOD = 100000
MOD5 = 3125  # 5^5
MOD2 = 32  # 2^5


def v_p(n: int, p: int) -> int:
    """Compute prime exponent v_p(n!) via Legendre's formula."""
    ans = 0
    while n > 0:
        ans += n // p
        n //= p
    return ans


# Precompute product of numbers <= 3125 coprime to 5
coprime_5_prod = [1] * (MOD5 + 1)
curr = 1
for i in range(1, MOD5 + 1):
    if i % 5 != 0:
        curr = (curr * i) % MOD5
    coprime_5_prod[i] = curr

P_block = coprime_5_prod[MOD5]


def non_5_part_mod5(n: int) -> int:
    """Compute N! / 5^(v_5(N!)) mod 3125 recursively in O(log_5 N) time."""
    if n == 0:
        return 1
    blocks = n // MOD5
    rem = n % MOD5
    block_contrib = pow(P_block, blocks, MOD5)
    rem_contrib = coprime_5_prod[rem]
    return (block_contrib * rem_contrib * non_5_part_mod5(n // 5)) % MOD5


def solve(n: int = 1000000000000) -> int:
    """Find the last five non-zero digits of N! for N = 10^12.

    Mathematical Principles Applied:
    1. Trailing Zeros Elimination:
       The last non-zero 5 digits of N! correspond to N! / 10^{v_5(N!)} mod 100,000.
       v_2(N!) = v_p(N!, 2) and v_5(N!) = v_p(N!, 5).
       Since v_2(N!) > v_5(N!) + 5 for N = 10^12, the expression modulo 2^5 = 32 is 0! (m2 = 0).

    2. Modulo 5^5 = 3125 Evaluation via Block Product Recurrence:
       N! / 5^{v_5(N!)} mod 3125 is computed in O(log_5 N) time using precomputed block product of numbers coprime to 5.
       Divide out 2^{v_5(N!)} modulo 3125 via modular inverse `pow(2, -1, 3125)`.

    3. Chinese Remainder Theorem (CRT):
       Combine m2 = 0 (mod 32) and m5 (mod 3125) to solve x (mod 100,000):
       x = (m5 + 3125 * ((0 - m5) * inv_3125_32 mod 32)) mod 100,000.

    Time Complexity: O(log_5 N * log MOD5) executing in ~0.0001s.
    Space Complexity: O(MOD5) memory for precomputed block table.
    """
    v2 = v_p(n, 2)
    v5 = v_p(n, 5)

    # Exponent difference v2 - v5 >= 5 implies m2 = N! / 10^v5 == 0 (mod 32)
    rem_2s = v2 - v5
    if rem_2s >= 5:
        m2 = 0
    else:
        prod = 1
        for i in range(1, n + 1):
            prod *= i
        while prod % 10 == 0:
            prod //= 10
        return prod % MOD

    # Evaluate N! / 5^v5 mod 3125
    n5 = non_5_part_mod5(n)
    inv2 = pow(2, -1, MOD5)
    m5 = (n5 * pow(inv2, v5, MOD5)) % MOD5

    # Reconstruct modulo 100,000 via Chinese Remainder Theorem
    inv_3125_32 = pow(MOD5, -1, MOD2)
    x = (m5 + MOD5 * ((m2 - m5) * inv_3125_32 % MOD2)) % MOD

    # Return last 5 non-zero digits of (10^12)!
    return x


if __name__ == "__main__":
    print(solve())
