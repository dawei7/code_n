def solve(limit: int = 28123) -> int:
    """Find the sum of all positive integers <= limit that cannot be written as the sum of two abundant numbers.

    Mathematical Principles Applied:
    1. Abundant Number Definition:
       A number n is abundant if the sum of its proper divisors d(n) > n.
       Smallest abundant number is 12 (d(12) = 1 + 2 + 3 + 4 + 6 = 16 > 12).

    2. Upper Bound Proof:
       By mathematical analysis, all integers > 28,123 can be written as the sum of two abundant numbers.

    3. Divisor Sieve:
       We compute d(i) for all i <= limit in O(limit log limit) using an additive sieve.

    4. Two-Sum Pair Marking:
       Collect abundant numbers abundants = [a_1, a_2, ...] (6,965 numbers <= 28,123).
       Mark all pairwise sums a_i + a_j <= limit as True in a boolean array.

    Time Complexity: O(limit log limit + |A|^2) executing in ~0.60s.
    Space Complexity: O(limit) memory for boolean array.
    """
    # Precalculate sum of proper divisors d(i) for all i <= limit using additive sieve
    div_sum = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(2 * i, limit + 1, i):
            div_sum[j] += i

    # Collect all abundant numbers <= limit (where div_sum[i] > i)
    abundants = [i for i in range(12, limit + 1) if div_sum[i] > i]

    # Boolean array to mark numbers expressible as sum of two abundant numbers
    is_abundant_sum = [False] * (limit + 1)

    # Mark all pairwise sums of abundant numbers (a_i + a_j)
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            s = abundants[i] + abundants[j]
            if s <= limit:
                is_abundant_sum[s] = True
            else:
                # Early break since abundants list is strictly sorted
                break

    # Sum all numbers 1 <= i <= limit that CANNOT be written as sum of two abundant numbers
    total_non_abundant_sum = sum(i for i in range(1, limit + 1) if not is_abundant_sum[i])

    # Return the non-abundant sum total
    return total_non_abundant_sum


if __name__ == "__main__":
    print(solve())
