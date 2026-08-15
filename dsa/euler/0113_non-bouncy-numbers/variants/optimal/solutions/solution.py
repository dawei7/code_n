def solve(d: int = 100) -> int:
    """Find the number of non-bouncy numbers below 10^d (10^100) using dynamic digit DP transitions.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Non-Bouncy Classification:
       A positive integer is non-bouncy if it is either increasing (non-decreasing digits)
       or decreasing (non-increasing digits).

    2. Dynamic Digit DP State Transitions:
       Let inc[j] be the number of increasing digit suffixes starting with digit j in {0..9}.
       Let dec[j] be the number of decreasing digit suffixes starting with digit j in {0..9}.
       For each digit position length step 1..d:
       - inc_next[j] = sum(inc[j:]) (next digit must be >= j)
       - dec_next[j] = sum(dec[:j+1]) (next digit must be <= j)

    3. Accumulation & Inclusion-Exclusion Overlap:
       - Non-empty increasing numbers: sum(inc[1:]) for each length step.
       - Non-empty decreasing numbers: sum(dec) - dec[0] for each length step.
       - Numbers with all identical digits (e.g. 11, 222, 7777) are counted in both sets.
         There are 9 such numbers for each length in 1..d (overlap = 9 * d).

    4. Total Non-Bouncy Count:
       NonBouncy(10^d) = total_increasing + total_decreasing - overlap.

    Complexity:
    -----------
    - Time Complexity: O(10 * d) = 1000 operations (executes in ~0.0001s).
    - Space Complexity: O(1) constant auxiliary space (10-element state arrays).
    """
    # DP arrays for increasing and decreasing digit suffix states
    inc = [1] * 10
    dec = [1] * 10

    total_inc = 0
    total_dec = 0

    for _ in range(d):
        # Accumulate valid positive non-decreasing numbers (starting with non-zero digit)
        total_inc += sum(inc[1:])

        # Accumulate valid positive non-increasing numbers (excluding all-zero prefix)
        total_dec += sum(dec) - dec[0]

        # Dynamic state transitions for next digit position
        new_inc = [sum(inc[j:]) for j in range(10)]
        new_dec = [sum(dec[: j + 1]) for j in range(10)]
        inc, dec = new_inc, new_dec

    # Subtract overlap of constant-digit numbers (9 numbers per length)
    overlap = 9 * d
    return total_inc + total_dec - overlap


if __name__ == "__main__":
    print(solve())
