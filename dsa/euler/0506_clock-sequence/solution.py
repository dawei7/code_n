"""Project Euler Problem 506: Clock Sequence.

Mathematical Formulation:
Clock sequence: 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, ...
Period length: 6 digits [1, 2, 3, 4, 3, 2] with sum 15.
Compute S(10^{14}) = sum_{n=1}^{10^{14}} v_n mod 1000000007 via periodic geometric series.
"""

from __future__ import annotations


def solve(n_limit: int = 10**14, mod: int = 1000000007) -> str:
    """Compute S(10^14) mod (10^9+7)."""
    seq = [1, 2, 3, 4, 3, 2]
    
    # Precompute v(r) and lengths for r in 1..15
    v_base = [0] * 16
    v_len = [0] * 16
    
    for r in range(1, 16):
        digits = []
        curr_sum = 0
        idx = 0
        while curr_sum < r:
            d = seq[idx % 6]
            digits.append(d)
            curr_sum += d
            idx += 1
        val = 0
        for d in digits:
            val = (val * 10 + d) % mod
        v_base[r] = val
        v_len[r] = len(digits)

    q = n_limit // 15
    rem = n_limit % 15
    
    p10_6 = pow(10, 6, mod)
    inv_p10_6 = pow(p10_6 - 1, mod - 2, mod)
    cycle_val = 123432 % mod
    
    total = 0
    for r in range(1, 16):
        count = q + (1 if (rem > 0 and r <= rem) else 0)
        if count <= 0:
            continue
            
        base_term = v_base[r]
        geom_sum = (pow(p10_6, count, mod) - 1) * inv_p10_6 % mod
        p10_len = pow(10, v_len[r], mod)
        
        # Contribution of base terms + repeated cycles
        # sum_{k=0}^{count-1} (cycle_val * (10^{6k} - 1)/(10^6 - 1) * 10^{len} + base)
        sum_cycles = (geom_sum - count) % mod * inv_p10_6 % mod
        term = (base_term * (count % mod) + cycle_val * p10_len % mod * sum_cycles) % mod
        total = (total + term) % mod
        
    return str(total % mod)


if __name__ == "__main__":
    print(solve())
