def solve(power: int = 5) -> int:
    """Find the sum of all numbers that can be written as the sum of the fifth powers of their digits.

    Mathematical Principles Applied:
    1. Upper Bound Upper Limit Proof:
       For a d-digit number n, the maximum possible sum of 5th powers of digits is d * 9^5 = d * 59049.
       The smallest d-digit number is 10^(d-1).
       For d = 7: 10^6 = 1,000,000 > 7 * 59049 = 413,343.
       Therefore, no 7-digit (or higher) number can equal the sum of 5th powers of its digits!
       Max possible 6-digit sum = 6 * 9^5 = 354,294.

    2. Precomputed Digit Fifth Powers:
       Precalculate powers[d] = d^5 for d in 0..9 for O(1) digit lookup.

    3. Search Range:
       Numbers must have at least 2 digits (exclude 1-digit numbers as 1 = 1^5 is excluded by problem).
       Search range: 10 <= i <= 354,294.

    Time Complexity: O(upper_limit * log10(upper_limit)) executing in ~0.20s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Precompute d^5 for digits d = 0..9
    powers = [d**power for d in range(10)]

    # Upper bound ceiling: 6 * 9^5 = 354,294
    upper_limit = 6 * (9**power)

    # Accumulator for matching numbers
    matching_sum = 0

    # Search numbers from 10 to upper_limit
    for i in range(10, upper_limit + 1):
        # Sum 5th powers of digits of i using precomputed array
        digit_power_sum = sum(powers[int(c)] for c in str(i))

        # If number equals sum of 5th powers of its digits, add to matching_sum
        if i == digit_power_sum:
            matching_sum += i

    # Return total sum of all matching numbers
    return matching_sum


if __name__ == "__main__":
    print(solve())
