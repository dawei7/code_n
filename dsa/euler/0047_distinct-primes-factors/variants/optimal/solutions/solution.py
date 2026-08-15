def solve(consecutive: int = 4, target_factors: int = 4) -> int:
    """Find the first of four consecutive integers to each have four distinct prime factors.

    Mathematical Principles Applied:
    1. Distinct Prime Factor Counting Sieve (Omega Function omega(n)):
       Let omega(n) be the number of distinct prime factors of n.
       We allocate array factors[i] up to limit = 200,000.
       For each prime i, increment factors[j] for all multiples j = i, 2i, 3i, ...
       This populates omega(x) for all x <= limit in O(limit log log limit) steps.

    2. Consecutive Sequence Scan:
       Scan x from 2 to limit, tracking consecutive run count where factors[x] == 4.
       When count == 4, return x - 3.

    Time Complexity: O(limit log log limit) executing in ~0.036s.
    Space Complexity: O(limit) memory to store factor count array.
    """
    limit = 200000

    # Allocate sieve array for distinct prime factor counts omega(x)
    factors = [0] * limit

    # Execute omega sieve: increment multiple positions for each prime i
    for i in range(2, limit):
        if factors[i] == 0:  # i is prime
            for j in range(i, limit, i):
                factors[j] += 1

    # Track consecutive run length of numbers with exactly 4 distinct prime factors
    count = 0
    for i in range(2, limit):
        if factors[i] == target_factors:
            count += 1
            # When 4 consecutive numbers are found, return the first number in the sequence
            if count == consecutive:
                return i - consecutive + 1
        else:
            count = 0

    return -1


if __name__ == "__main__":
    print(solve())
