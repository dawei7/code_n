def solve(limit: int = 10000) -> int:
    """Compute the sum of all amicable numbers strictly under limit.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Proper Divisor Sum Function:
       Let d(n) denote the sum of proper divisors of n (divisors strictly less than n):
           d(n) = sum_{k | n, k < n} k = sigma_1(n) - n

    2. Amicable Numbers & Pairs:
       Two distinct integers a and b form an amicable pair if:
           d(a) = b  and  d(b) = a,  with a != b
       Each integer in an amicable pair is called an amicable number.

    3. Divisor Sieve Algorithm:
       We compute d(n) for all n in [1, limit - 1] in O(limit log limit) time by sieving:
       For each integer i in [1, limit - 1], add i to all multiples 2i, 3i, ... < limit.

    Complexity:
    -----------
    - Time Complexity: O(limit log limit) harmonic sieve (~0.002s).
    - Space Complexity: O(limit) array storage (~80 KB).
    """
    # Sieve of proper divisor sums up to limit
    d = [0] * limit
    for i in range(1, limit):
        for j in range(2 * i, limit, i):
            d[j] += i

    # Identify and accumulate all amicable numbers
    amicable_sum = 0
    for a in range(2, limit):
        b = d[a]
        if b != a and b < limit and d[b] == a:
            amicable_sum += a

    return amicable_sum


if __name__ == "__main__":
    print(solve())
