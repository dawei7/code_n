"""Project Euler Problem 506: Clock Sequence.

Find S(10^14) mod 123454321, where S(n) = sum_{k=1..n} v_k for the clock digit sequence.
"""

from typing import List

MOD = 123454321


def solve(n: int = 10**14, mod: int = MOD) -> int:
    """Compute S(n) mod mod using 15-period clock block geometric progression sum."""
    digits = [1, 2, 3, 4, 3, 2]
    v_list: List[int] = []
    p_list: List[int] = []
    idx = 0

    for k in range(1, 16):
        start_idx = idx % 6
        cur_sum = 0
        cur_str = ""
        while cur_sum < k:
            d = digits[idx % 6]
            cur_sum += d
            cur_str += str(d)
            idx += 1
        v_list.append(int(cur_str))

        block_str = "".join(
            str(digits[(start_idx + i) % 6]) for i in range(6)
        )
        p_list.append(int(block_str))

    q_full = n // 15
    rem = n % 15

    total = 0
    inv_den = pow(10**6 - 1, -1, mod)

    for r_idx in range(15):
        q = q_full + (1 if r_idx < rem else 0)
        if q == 0:
            continue

        vr = v_list[r_idx] % mod
        pr = p_list[r_idx] % mod
        len_vr = len(str(v_list[r_idx]))

        t1 = (q % mod) * vr % mod

        scale = (pr * pow(10, len_vr, mod)) % mod
        geom_sum = (pow(10, 6 * q, mod) - 1) * inv_den % mod
        geom_diff = (geom_sum - (q % mod)) % mod
        t2 = scale * geom_diff % mod * inv_den % mod

        total = (total + t1 + t2) % mod

    return total


if __name__ == "__main__":
    print(solve())
