"""Project Euler Problem 373: Circumscribed Circles.

Find the sum of the circumradii of all integer-sided triangles with integer circumradius <= 10^7.
"""

from typing import List


def solve(limit: int = 10000000) -> int:
    """Compute S(limit) via linear multiplicative sieve of Gaussian prime power components."""
    if limit < 5:
        return 0

    primes: List[int] = []
    is_prime = bytearray([1]) * (limit + 1)

    # Multiplicative components for A(r), B(r), C(r)
    f_a = [1] * (limit + 1)
    f_b = [1] * (limit + 1)
    f_c = [1] * (limit + 1)
    pe_arr = [0] * (limit + 1)
    e_arr = bytearray([0]) * (limit + 1)

    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            e_arr[i] = 1
            pe_arr[i] = i
            if i % 4 == 1:
                f_a[i] = i * 7  # 3(1)^2 + 3(1) + 1 = 7
                f_b[i] = i * 3  # 2(1) + 1 = 3
                f_c[i] = i * 1  # 2(0) + 1 = 1
            else:
                f_a[i] = i
                f_b[i] = i
                f_c[i] = i

        for p in primes:
            ip = i * p
            if ip > limit:
                break
            is_prime[ip] = 0

            if i % p == 0:
                new_e = e_arr[i] + 1
                new_pe = pe_arr[i] * p
                e_arr[ip] = new_e
                pe_arr[ip] = new_pe

                rest = ip // new_pe
                if p % 4 == 1:
                    val_a = new_pe * (3 * new_e * new_e + 3 * new_e + 1)
                    val_b = new_pe * (2 * new_e + 1)
                    val_c = new_pe * (2 * (new_e // 2) + 1)
                else:
                    val_a = new_pe
                    val_b = new_pe
                    val_c = new_pe

                f_a[ip] = f_a[rest] * val_a
                f_b[ip] = f_b[rest] * val_b
                f_c[ip] = f_c[rest] * val_c
                break
            else:
                e_arr[ip] = 1
                pe_arr[ip] = p
                f_a[ip] = f_a[i] * f_a[p]
                f_b[ip] = f_b[i] * f_b[p]
                f_c[ip] = f_c[i] * f_c[p]

    sum_a = sum(f_a[1:])
    sum_b = sum(f_b[1:])
    sum_c = sum(f_c[1:])
    sum_r = limit * (limit + 1) // 2

    # S(n) = (2 * sum_a - 3 * sum_b + 3 * sum_c - 2 * sum_r) // 6
    return (2 * sum_a - 3 * sum_b + 3 * sum_c - 2 * sum_r) // 6


if __name__ == "__main__":
    print(solve())
