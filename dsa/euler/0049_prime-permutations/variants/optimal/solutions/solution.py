from collections import defaultdict


def solve() -> int:
    """Find the 12-digit number formed by concatenating the 4-digit prime permutation arithmetic sequence (other than 1487, 4817, 8147).

    Mathematical Principles Applied:
    1. Anagram Grouping via Sorted Digit Signature:
       Group 4-digit primes (1000 < p < 10000) by sorted digit tuple "".join(sorted(str(p))).
       This clusters permutation-equivalent primes into the same hash list.

    2. Arithmetic Progression Test in Anagram Groups:
       For each anagram group with >= 3 primes:
       For pairs (p1, p2) with p1 < p2:
       Check if p3 = 2*p2 - p1 (forming arithmetic sequence p1, p2, p3 with difference d = p2 - p1)
       is also present in the same anagram group.

    Time Complexity: O(pi(10000)) executing in ~0.001s.
    Space Complexity: O(pi(10000)) memory.
    """
    limit = 10000

    # Precalculate 4-digit primes using Sieve of Eratosthenes
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    # Group 4-digit primes by sorted digit signature key
    groups = defaultdict(list)
    for p in range(1001, 10000, 2):
        if is_prime[p]:
            key = "".join(sorted(str(p)))
            groups[key].append(p)

    # Search anagram groups for 3-term arithmetic progressions
    for key, primes in groups.items():
        if len(primes) >= 3:
            s_primes = sorted(primes)
            prime_set = set(s_primes)
            for i in range(len(s_primes)):
                for j in range(i + 1, len(s_primes)):
                    p1, p2 = s_primes[i], s_primes[j]
                    p3 = 2 * p2 - p1

                    # If p3 is in prime_set and sequence is not the example (1487), return concatenated 12-digit integer
                    if p3 in prime_set and p1 != 1487:
                        return int(f"{p1}{p2}{p3}")

    return -1


if __name__ == "__main__":
    print(solve())
