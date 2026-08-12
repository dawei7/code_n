MOD = 100000
MOD5 = 3125  # 5^5
MOD2 = 32    # 2^5


def v_p(n: int, p: int) -> int:
    """Compute prime exponent v_p(n!)."""
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
    """Compute N! / 5^(v_5(N!)) mod 3125."""
    if n == 0:
        return 1
    blocks = n // MOD5
    rem = n % MOD5
    block_contrib = pow(P_block, blocks, MOD5)
    rem_contrib = coprime_5_prod[rem]
    return (block_contrib * rem_contrib * non_5_part_mod5(n // 5)) % MOD5


def solve(n: int = 1000000000000) -> int:
    """Find last five non-zero digits of n!.
    
    Time Complexity: O(log_5(N) * log(MOD5))
    Space Complexity: O(MOD5)
    """
    v2 = v_p(n, 2)
    v5 = v_p(n, 5)

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

    # N! / 5^v5 mod 3125:
    n5 = non_5_part_mod5(n)
    inv2 = pow(2, -1, MOD5)
    m5 = (n5 * pow(inv2, v5, MOD5)) % MOD5

    # Chinese Remainder Theorem: x = m2 mod 32, x = m5 mod 3125
    inv_3125_32 = pow(MOD5, -1, MOD2)
    x = (m5 + MOD5 * ((m2 - m5) * inv_3125_32 % MOD2)) % MOD
    return x
