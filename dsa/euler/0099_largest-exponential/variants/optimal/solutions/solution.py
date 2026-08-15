import math
import os


def solve(filepath: str = "") -> int:
    """Find the 1-indexed line number in base_exp.txt with the largest numerical value b^e using logarithms.

    Mathematical Principles Applied:
    1. Logarithmic Monotonicity Transformation:
       Since the natural logarithm log(x) is a strictly monotonically increasing function on (0, inf),
       b1^e1 > b2^e2  <=>  log(b1^e1) > log(b2^e2)  <=>  e1 * log(b1) > e2 * log(b2).

    2. Avoiding Astronomical Exponentiation:
       Calculating b^e directly (where b ~ 10^6 and e ~ 10^6) results in numbers with millions of digits.
       Computing floating-point log values e * log(b) takes O(1) time per line and prevents memory overflow.

    Time Complexity: O(N) where N = 1000 lines (executes in ~0.001s).
    Space Complexity: O(N) memory to store line data.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0099_largest-exponential/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "base_exp.txt")

    # Read base_exp text file
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip().split(",") for line in f if line.strip()]

    max_val = 0.0
    best_line = 0

    # Scan lines and evaluate e * log(b)
    for idx, (base_s, exp_s) in enumerate(lines, 1):
        b, e = int(base_s), int(exp_s)
        val = e * math.log(b)

        # Update maximum log magnitude and corresponding 1-indexed line number
        if val > max_val:
            max_val = val
            best_line = idx

    # Return 1-indexed line number of maximum exponential pair
    return best_line


if __name__ == "__main__":
    print(solve())
