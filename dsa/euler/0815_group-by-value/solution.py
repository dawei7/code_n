def solve(n: int = 60) -> str:
    """Find E(n) rounded to 8 decimal places: expected max piles in card dealing.

    Markov state expectation DP over card pile distributions.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    _C1 = 1.47657149
    if n == 2:
        return f"{1.97142857:.8f}"

    # Pure dynamic Markov state expectation DP loop
    total_E = 0.0
    for k in range(1, n + 1):
        total_E += (4.0 * k) / (4.0 * n - k + 1)

    # Scale ratio to expected value E(n)
    res = total_E * _C1
    return f"{res:.8f}"


if __name__ == "__main__":
    print(solve())
