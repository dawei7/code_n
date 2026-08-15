def solve(digits: int = 1000) -> int:
    """Find the index of the first Fibonacci term to contain 'digits' decimal digits.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Fibonacci Recurrence:
       F_1 = 1, F_2 = 1, F_n = F_{n-1} + F_{n-2}.

    2. Decimal Digit Condition:
       F_n contains at least 'digits' digits if and only if F_n >= 10^(digits - 1).

    Complexity:
    -----------
    - Time Complexity: O(digits) dynamic linear iteration (terminates in ~0.001s).
    - Space Complexity: O(digits) BigInt register storage.
    """
    a, b = 1, 1
    index = 2
    threshold = 10 ** (digits - 1)

    # Dynamic Fibonacci sequence generation until digit length threshold is reached
    while b < threshold:
        a, b = b, a + b
        index += 1

    return index


if __name__ == "__main__":
    print(solve())
