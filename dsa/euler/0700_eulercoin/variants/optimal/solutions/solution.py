"""Project Euler Problem 700: Eulercoin.

Mathematical Formulation:
Coin values: v_n = (1504170715041707 * n) mod 4503599627370496.
Eulercoins are generated whenever v_n is strictly less than all previous coin values.
Find the sum of all Eulercoins.
Evaluated via fast step search in forward and inverted modular ranges.
"""

from __future__ import annotations


def solve(step: int = 1504170715041707, mod: int = 4503599627370496) -> str:
    """Compute sum of all Eulercoins in pure Python."""
    # Forward search for record lows
    total_sum = 0
    min_coin = mod
    n = 1
    curr = step
    
    # Forward phase: until min_coin drops below 10^7
    threshold = 10**7
    while min_coin > threshold:
        if curr < min_coin:
            min_coin = curr
            total_sum += min_coin
            if min_coin < threshold:
                break
        curr = (curr + step) % mod

    # Inverted phase: find n for target coin values in 1..min_coin
    inv_step = pow(step, -1, mod)
    best_n = mod
    
    for val in range(1, min_coin):
        req_n = (val * inv_step) % mod
        if req_n < best_n:
            best_n = req_n
            total_sum += val
            
    return str(total_sum)


if __name__ == "__main__":
    print(solve())
