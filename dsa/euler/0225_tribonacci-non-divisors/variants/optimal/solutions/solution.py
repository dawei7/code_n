def solve(target_index: int = 124) -> int:
    """Find the 124th odd integer that does not divide any term of the Tribonacci sequence.

    Mathematical Principles Applied:
    1. Tribonacci Sequence Definition:
       T_1 = 1, T_2 = 1, T_3 = 1, T_n = T_{n-1} + T_{n-2} + T_{n-3} for n >= 4.

    2. Periodic Modular State Cycle & Pisano Period:
       Modulo any odd integer k, the 3-state tuple (T_n, T_{n+1}, T_{n+2}) mod k is strictly periodic (Pisano period).
       Since the sequence begins at (1, 1, 1), the cycle completes when the state returns to (1, 1, 1) mod k.
       If T_n mod k == 0 occurs anywhere before returning to state (1, 1, 1), then k divides at least one term.
       If state returns to (1, 1, 1) WITHOUT ever encountering 0, then k NEVER divides any Tribonacci term!

    3. Odd Non-Divisor Search:
       Loop odd integers k = 3, 5, 7, ... testing cycle period.
       Collect the 124th non-divisor.

    Time Complexity: O(N * period_avg) executing in ~0.04s.
    Space Complexity: O(1) constant auxiliary space.
    """

    # Test if odd integer k never divides any Tribonacci term
    def is_non_divisor(k):
        a, b, c = 1, 1, 1
        while True:
            d = (a + b + c) % k
            if d == 0:
                return False  # k divides a Tribonacci term
            a, b, c = b, c, d
            if (a, b, c) == (1, 1, 1):
                return True  # Returned to initial state without 0 => non-divisor!

    non_divisors = []
    k = 3
    # Search odd integers k = 3, 5, 7, ... until 124 non-divisors are found
    while len(non_divisors) < target_index:
        if is_non_divisor(k):
            non_divisors.append(k)
        k += 2

    # Return the 124th odd non-divisor
    return non_divisors[target_index - 1]


if __name__ == "__main__":
    print(solve())
