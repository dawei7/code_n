def solve(limit: int = 1000000000000) -> int:
    """Find the number of blue discs b in the first arrangement with total discs N > limit (10^12) where P(BB) = 1/2.

    Mathematical Principles Applied:
    1. Probability Equation for Two Blue Discs:
       P(BB) = (b / N) * ((b - 1) / (N - 1)) = 1 / 2.
       Cross-multiplying:
       2 * b * (b - 1) = N * (N - 1) => 2b^2 - 2b = N^2 - N.

    2. Pell-Type Diophantine System:
       Completing the square:
       8b^2 - 8b + 1 = 4N^2 - 4N + 1 => 2(2b - 1)^2 - 1 = (2N - 1)^2.
       Let X = 2N - 1 and Y = 2b - 1. Then X^2 - 2Y^2 = -1 (Pell's Equation).

    3. Fundamental Matrix Linear Recurrence:
       The integer solutions (b_k, N_k) satisfy the matrix recurrence:
       b_{k+1} = 3 * b_k + 2 * N_k - 2
       N_{k+1} = 4 * b_k + 3 * N_k - 3
       with base seed (b_1, N_1) = (15, 21).

    Time Complexity: O(log limit) logarithmic execution in ~0.0000s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Initial seed solution: 15 blue discs in a total of 21 discs (P(BB) = 15/21 * 14/20 = 1/2)
    b, n = 15, 21

    # Advance linear recurrence until total discs n exceeds 1,000,000,000,000 (10^12)
    while n <= limit:
        b_next = 3 * b + 2 * n - 2
        n_next = 4 * b + 3 * n - 3
        b, n = b_next, n_next

    # Return number of blue discs b for the first arrangement with N > 10^12
    return b


if __name__ == "__main__":
    print(solve())
