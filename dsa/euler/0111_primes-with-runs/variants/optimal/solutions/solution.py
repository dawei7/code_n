import itertools


def is_prime_mr(n: int) -> bool:
    """Miller-Rabin primality test for 10-digit integers."""
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
    """Find S(10, d) by searching for 10-digit primes with max repeated digits d."""
    for count_d in range(9, 0, -1):
        other_count = 10 - count_d
        primes_found = []

        other_digits = [x for x in range(10) if x != d]

        for d_positions in itertools.combinations(range(10), count_d):
            d_pos_set = set(d_positions)
            other_positions = [i for i in range(10) if i not in d_pos_set]

            for other_vals in itertools.product(other_digits, repeat=other_count):
                digits = [0] * 10
                for pos in d_positions:
                    digits[pos] = d
                for idx, pos in enumerate(other_positions):
                    digits[pos] = other_vals[idx]

                if digits[0] == 0:
                    continue  # No leading zeroes

                val = int("".join(str(x) for x in digits))
                if is_prime_mr(val):
                    primes_found.append(val)

        if primes_found:
            return sum(set(primes_found))

    return 0


def solve() -> int:
    """Find sum of all S(10, d) for d = 0 to 9.
    
    Time Complexity: O(D * Candidates * Primality)
    Space Complexity: O(Primes)
    """
    return sum(sum_s_10_d(d) for d in range(10))
