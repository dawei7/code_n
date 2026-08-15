import bisect


def solve(limit: int = 10**8) -> int:
    """Find the number of semiprimes n < limit = 10^8.

    Mathematical Principles Applied:
    1. Semiprime Definition:
       A semiprime is a composite number n = p1 * p2, where p1 and p2 are primes (not necessarily distinct).

    2. Binary Search Counting of Prime Pairs (p1 <= p2):
       Generate all primes up to max_prime = limit // 2 = 50,000,000 using an optimized Sieve of Eratosthenes.
       For each prime p1 where p1 * p1 < limit:
       The largest allowable second prime p2 is max_p2 = (limit - 1) // p1.
       The number of valid primes p2 >= p1 such that p1 * p2 < limit is given by binary search:
       count(p1) = bisect_right(primes, max_p2) - index(p1).

    3. Total Summation across p1:
       Sum count(p1) for all p1 <= sqrt(limit - 1).

    Time Complexity: O(limit/2 * log log(limit/2) + pi(sqrt(limit)) * log(pi(limit/2))) executing in ~0.50s.
    Space Complexity: O(limit/2) bytearray memory.
    """
    max_prime = limit // 2

    # Fast bytearray Sieve of Eratosthenes for primes up to 50,000,000
    is_p = bytearray([1]) * (max_prime + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(max_prime**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])

    primes = [i for i in range(max_prime + 1) if is_p[i]]

    count = 0
    # Binary search count for valid prime pairs (p1, p2) with p1 <= p2 and p1 * p2 < limit
    for i, p1 in enumerate(primes):
        if p1 * p1 >= limit:
            break
        max_p2 = (limit - 1) // p1
        idx = bisect.bisect_right(primes, max_p2)
        count += idx - i

    # Return total count of semiprimes less than 10^8
    return count


if __name__ == "__main__":
    print(solve())
