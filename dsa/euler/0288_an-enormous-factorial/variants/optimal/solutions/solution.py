def solve(p: int = 61, q: int = 10**7, k_power: int = 10) -> int:
    """Find NF(61, 10^7) mod 61^10 for N(61, 10^7)!.
    
    Time Complexity: O(q) via Legendre's Formula & Modular Reduction
    Space Complexity: O(k_power)
    """
    mod_val = p**k_power
    inv = pow(p - 1, -1, mod_val)
    c_val = (-inv) % mod_val

    v_n = [
        (pow(p, n) - 1) // (p - 1) % mod_val for n in range(1, k_power)
    ]

    S = 290797
    tot = 0

    for n in range(1, q + 1):
        S = (S * S) % 50515093
        T_n = S % p
        if T_n == 0:
            continue

        if n < k_power:
            tot = (tot + T_n * v_n[n - 1]) % mod_val
        else:
            tot = (tot + T_n * c_val) % mod_val

    return tot
