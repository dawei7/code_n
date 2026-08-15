import math
import os


def is_triangle_number(t: int) -> bool:
    """Check if t is a triangle number (8t + 1 is a perfect odd square)."""
    val = 8 * t + 1
    root = math.isqrt(val)
    return root * root == val


def solve(filepath: str = "") -> int:
    """Count how many words in words.txt are triangle words.

    Mathematical Principles Applied:
    1. Inverse Triangle Test:
       A word value V = sum_{c in W} (ord(c) - 64) is a triangle number iff
       1/2 * n * (n + 1) = V => n^2 + n - 2V = 0 => n = (-1 + sqrt(1 + 8V)) / 2.
       Therefore, V is a triangle number iff 1 + 8V is a perfect square!

    2. Offline Word List Parsing:
       Parse quote-delimited words from package-local words.txt file.

    Time Complexity: O(W * L) where W = 1786 words and L ≈ 6.
    Space Complexity: O(W * L) memory to store word list.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0042_coded-triangle-numbers/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "words.txt")

    # Read words text file
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Extract word strings
    words = [w.strip('"') for w in text.strip().split(",") if w.strip()]

    # Count words whose alphabetical character value sum is a triangle number
    triangle_count = 0
    for w in words:
        val = sum(ord(c) - 64 for c in w.upper() if "A" <= c <= "Z")
        if is_triangle_number(val):
            triangle_count += 1

    # Return total count of triangle words
    return triangle_count


if __name__ == "__main__":
    print(solve())
