def solve(target_n: int = 30) -> int:
    """Find a_30, the 30th digit power sum number (an integer >= 10 equal to the sum of its digits raised to some power).

    Mathematical Principles Applied:
    1. Inverse Search Space Generation:
       Instead of searching huge numbers N and testing if the sum of digits of N raised to some power equals N,
       we iterate candidate digit sums (base in 2..100) and powers (e in 2..50).

    2. Digit Power Sum Condition:
       For a candidate val = base^e (val >= 10):
       Check if sum(digits(val)) == base.
       If True, insert val into a set of solutions to deduplicate.

    3. 30th Term Extraction:
       Sort the generated solutions set and return the 30th term (1-indexed, index 29).

    Time Complexity: O(BaseMax * ExpMax) executing in ~0.001s.
    Space Complexity: O(Solutions) memory for set.
    """
    results = set()

    # Iterate base digit sums in 2..100 and powers e in 2..50
    for base in range(2, 100):
        for e in range(2, 50):
            val = base**e
            if val >= 10:
                # Check if sum of decimal digits equals the base
                if sum(int(c) for c in str(val)) == base:
                    results.add(val)

    # Sort generated results in ascending order
    sorted_results = sorted(results)

    # Return the 30th digit power sum number (1-indexed)
    return sorted_results[target_n - 1]


if __name__ == "__main__":
    print(solve())
