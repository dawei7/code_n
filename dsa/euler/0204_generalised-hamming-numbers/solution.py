import math


def solve(type_n: int = 100, limit: int = 10**9) -> int:
    """Find the number of generalised Hamming numbers of type 100 <= 10^9.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Smooth Numbers Definition:
       A generalised Hamming number of type 100 (100-smooth number) is a positive integer whose prime
       factors are all <= 100.
       Primes <= 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
       73, 79, 83, 89, 97 (25 primes).

    2. Descending Search Ordering & Base Case O(1) Evaluation:
       By recursing over primes in DESCENDING order (97, 89, 83, ..., 3, 2):
       - Larger primes prune deeper branches immediately because their powers grow rapidly.
       - The final prime 2 can be evaluated in O(1) time using bit length:
         val * 2^k <= limit  <=>  k in [0, (limit // val).bit_length() - 1].
         This eliminates millions of recursive leaf calls!

    Complexity:
    -----------
    - Time Complexity: O(H(100, 10^9) / log 2) operations (~0.15s for limit = 10^9).
    - Space Complexity: O(pi(type_n)) recursion call stack depth (~25 frames).
    """
    max_p = type_n
    is_p = bytearray([1]) * (max_p + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(max_p**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])
    primes = [i for i in range(2, max_p + 1) if is_p[i]]

    # Recurse in descending order: 97, 89, ..., 2
    primes_desc = primes[::-1]
    n_p = len(primes_desc)

    def dfs(idx: int, val: int) -> int:
        if idx == n_p - 1:  # Base case for prime 2
            return (limit // val).bit_length()

        p = primes_desc[idx]
        cnt = 0
        v = val
        while v <= limit:
            cnt += dfs(idx + 1, v)
            v *= p
        return cnt

    return dfs(0, 1)


if __name__ == "__main__":
    print(solve())
