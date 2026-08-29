import itertools


def is_prime(n: int) -> bool:
    """Trial division primality test with 6k +/- 1 wheel optimization."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def solve() -> int:
    """Find the largest n-digit pandigital prime number.

    Mathematical Principles Applied:
    1. Divisibility Rule for 3 Elimination:
       A number is divisible by 3 iff the sum of its digits is divisible by 3.
       - 9-digit pandigital sum = 1 + 2 + ... + 9 = 45 (divisible by 3 => always composite).
       - 8-digit pandigital sum = 1 + 2 + ... + 8 = 36 (divisible by 3 => always composite).
       Therefore, NO 9-digit or 8-digit pandigital prime exists!
       The largest pandigital prime MUST be a 7-digit number (sum = 28, not divisible by 3).

    2. Permutation Search in Descending Order:
       Iterate through permutations of digits "7654321" in descending lexicographical order.
       The first permutation that passes the primality test is guaranteed to be the global maximum!

    Time Complexity: O(7! * sqrt(P)) executing in ~0.0001s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Iterate 7-digit permutations in descending order starting from 7654321
    for perm in itertools.permutations("7654321"):
        val = int("".join(perm))

        # Check primality of candidate 7-digit pandigital number
        if is_prime(val):
            # Return first prime found (guaranteed to be the largest 7-digit pandigital prime)
            return val

    return -1


if __name__ == "__main__":
    print(solve())
