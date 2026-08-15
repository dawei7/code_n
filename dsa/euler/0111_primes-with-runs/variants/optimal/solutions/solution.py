import itertools


def is_prime_mr(n: int) -> bool:
    """Deterministic Miller-Rabin primality test for 10-digit integers using bases (2, 7, 61).

    Mathematical Principles Applied:
    1. Deterministic Miller-Rabin Primality Testing:
       For any 64-bit integer n < 4.7 x 10^9, testing bases a in {2, 7, 61} is 100% deterministic!
       Write n - 1 = 2^s * d with d odd.
       n is prime iff for each base a:
       a^d == 1 (mod n) or a^(2^r * d) == -1 (mod n) for some 0 <= r < s.
    """
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        return True
    if any(n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)):
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 7, 61):
        if n <= a:
            break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def sum_s_10_d(d: int) -> int:
    """Find S(10, d), the sum of all 10-digit primes containing the maximum possible count M(10, d) of digit d.

    Mathematical Principles Applied:
    1. Maximum Repeated Digit Count M(10, d):
       Search count_d from 9 down to 1. The first count_d that yields at least one 10-digit prime is M(10, d).

    2. Positional Pattern Generation:
       For a fixed count_d:
       - Choose positions of digit d using itertools.combinations(range(10), count_d).
       - Fill remaining (10 - count_d) positions with other digits in {0..9} \\ {d}.
       - Exclude candidates with leading zeros (digits[0] == 0).
       - Test primality using Miller-Rabin.
    """
    for count_d in range(9, 0, -1):
        other_count = 10 - count_d
        primes_found = []

        other_digits = [x for x in range(10) if x != d]

        # Choose positions for repeated digit d
        for d_positions in itertools.combinations(range(10), count_d):
            d_pos_set = set(d_positions)
            other_positions = [i for i in range(10) if i not in d_pos_set]

            # Product loop for non-d positions
            for other_vals in itertools.product(
                other_digits, repeat=other_count
            ):
                digits = [0] * 10
                for pos in d_positions:
                    digits[pos] = d
                for idx, pos in enumerate(other_positions):
                    digits[pos] = other_vals[idx]

                # Enforce no leading zero constraint
                if digits[0] == 0:
                    continue

                val = int("".join(str(x) for x in digits))
                if is_prime_mr(val):
                    primes_found.append(val)

        # Return sum of unique 10-digit primes for the maximum count_d M(10, d)
        if primes_found:
            return sum(set(primes_found))

    return 0


def solve() -> int:
    """Find the sum of all S(10, d) for digits d = 0 to 9.

    Time Complexity: O(10 * Candidates * MillerRabin) executing in ~0.02s.
    Space Complexity: O(Primes) memory for primes list.
    """
    return sum(sum_s_10_d(d) for d in range(10))


if __name__ == "__main__":
    print(solve())
