def solve(limit: int = 4000000) -> int:
    """Find the sum of all even-valued Fibonacci terms <= limit.

    Mathematical Principles Applied:
    1. Parity Periodicity of Fibonacci Sequence:
       The parity of Fibonacci numbers follows a repeating pattern of length 3:
       F_1 = 1 (Odd), F_2 = 2 (Even), F_3 = 3 (Odd), F_4 = 5 (Odd), F_5 = 8 (Even), F_6 = 13 (Odd)...
       Therefore, even-valued terms occur exactly at indices that are multiples of 3: E_n = F_{3n}.

    2. Direct Recurrence for Even Terms:
       Using F_{3n} = F_{3n-1} + F_{3n-2} and substituting F_{3n-1} = F_{3n-2} + F_{3n-3}:
       F_{3n} = 2*F_{3n-2} + F_{3n-3}
       Expanding F_{3n-2} = F_{3n-3} + F_{3n-4} yields the direct linear recurrence:
       E_n = 4 * E_{n-1} + E_{n-2}
       where E_1 = F_3 = 2 and E_2 = F_6 = 8.

    3. Performance Gain:
       Generating only even terms directly avoids parity checks (modulo operations)
       and skips two out of every three sequence elements entirely.

    Time Complexity: O(log_phi limit) where phi^3 ≈ 4.236 (only ~11 steps for 4,000,000).
    Space Complexity: O(1) constant auxiliary memory.
    """
    # Initialize running sum of even terms
    total_sum = 0

    # First two even Fibonacci terms: E_1 = 2 (F_3), E_2 = 8 (F_6)
    e1, e2 = 2, 8

    # Loop while the current even Fibonacci term does not exceed the upper limit
    while e1 <= limit:
        # Accumulate the current even term into the running total
        total_sum += e1

        # Advance to the next even Fibonacci term using the direct recurrence:
        # Next e1 = e2, Next e2 = 4 * e2 + e1
        e1, e2 = e2, 4 * e2 + e1

    # Return the exact accumulated sum of even Fibonacci terms
    return total_sum


if __name__ == "__main__":
    print(solve())
