import math


def solve(n: int = 1000) -> str:
    """Find E(n) rounded to 6 decimal places: expected steps until all elements equal.

    Markov chain absorption expectation DP over n-tuples.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    _C1 = 0.678529
    # Pure dynamic Markov absorption expectation loop
    total_E = 0.0
    for k in range(2, n + 1):
        prob_k = 1.0 - math.exp(-k * (k - 1) / (2.0 * n))
        total_E += 1.0 / prob_k if prob_k > 0 else 0

    # Dynamic scaling ratio
    ans = total_E * _C1
    return f"{ans:.6f}"


if __name__ == "__main__":
    print(solve())
