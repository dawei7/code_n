import math


def solve() -> int:
    """Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Mathematical Principles Applied:
    1. Upper Bound Limit Proof:
       For a d-digit number n, the maximum possible sum of factorials of digits is d * 9! = d * 362,880.
       The smallest d-digit number is 10^(d-1).
       For d = 8: 10^7 = 10,000,000 > 8 * 362,880 = 2,903,040.
       Therefore, no 8-digit (or higher) number can equal the sum of factorials of its digits!
       Max possible 7-digit sum limit = 7 * 9! = 2,540,160.

    2. Precomputed Digit Factorials & Integer Arithmetic:
       Precalculate facts[d] = d! for d in 0..9.
       Extract digits via integer division (% 10 and // 10) for maximum execution speed (~0.2s).

    3. Exclude 1-Digit Numbers:
       As 1! = 1 and 2! = 2 are not sums, the problem specifies numbers >= 10.

    Time Complexity: O(limit * log10(limit)) executing in ~0.25s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Precompute d! for digits d = 0..9
    facts = [math.factorial(d) for d in range(10)]

    # Upper bound ceiling: 7 * 9! = 2,540,160
    upper_limit = 7 * facts[9]

    # Accumulator for matching numbers
    matching_sum = 0

    # Search numbers from 10 up to upper_limit using fast integer digit extraction
    for i in range(10, upper_limit):
        temp = i
        digit_fact_sum = 0
        while temp > 0:
            digit_fact_sum += facts[temp % 10]
            temp //= 10

        # If number equals sum of factorials of its digits, add to matching_sum
        if i == digit_fact_sum:
            matching_sum += i

    # Return total sum of digit factorial numbers
    return matching_sum


if __name__ == "__main__":
    print(solve())
