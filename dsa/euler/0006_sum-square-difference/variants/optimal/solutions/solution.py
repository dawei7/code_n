def solve(n: int = 100) -> int:
    """Compute the difference between the square of the sum and the sum of the squares.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Sum of First n Natural Numbers:
           S_1(n) = sum_{k=1}^n k = n * (n + 1) // 2
       Square of the sum:
           (S_1(n))^2 = [n^2 * (n + 1)^2] // 4

    2. Sum of the First n Squares (Pyramidal Numbers):
           S_2(n) = sum_{k=1}^n k^2 = [n * (n + 1) * (2n + 1)] // 6

    3. Closed-Form Difference:
           D(n) = (S_1(n))^2 - S_2(n)

    Complexity:
    -----------
    - Time Complexity: O(n) dynamic accumulation.
    - Space Complexity: O(1) constant auxiliary space.
    """
    # Dynamically accumulate sum of first n numbers and sum of squares
    sum_n = sum(range(1, n + 1))
    sum_squares = sum(k * k for k in range(1, n + 1))

    # Return difference between square of sum and sum of squares
    square_of_sum = sum_n * sum_n
    return square_of_sum - sum_squares


if __name__ == "__main__":
    print(solve())
