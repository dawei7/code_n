import os
import re


def solve(filepath: str = "") -> int:
    """Find the number of characters saved by simplifying Roman numerals in roman.txt using regex replacements.

    Mathematical Principles Applied:
    1. Minimal Roman Numeral String Representation:
       Minimal Roman numerals use subtractive notation to shorten sub-strings:
       - VIIII (5 chars) -> IX (2 chars): saves 3 chars.
       - IIII (4 chars) -> IV (2 chars): saves 2 chars.
       - LXXXX (5 chars) -> XC (2 chars): saves 3 chars.
       - XXXX (4 chars) -> XL (2 chars): saves 2 chars.
       - DCCCC (5 chars) -> CM (2 chars): saves 3 chars.
       - CCCC (4 chars) -> CD (2 chars): saves 2 chars.

    2. Equivalence of Subtraction Reduction:
       Since each pair replacement reduces the string length by exactly the character count difference
       (e.g., VIIII -> IX saves 3, IIII -> IV saves 2), we can perform regex pattern substitutions
       or parse values to compute exact minimal length.

    Time Complexity: O(N * L) where N = 1000 lines (executes in ~0.001s).
    Space Complexity: O(N * L) memory for text buffer.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0089_roman-numerals/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "roman.txt")

    # Read roman text file
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    # Regular expression matching un-subtracted Roman numeral patterns
    pattern = re.compile(r"VIIII|IIII|LXXXX|XXXX|DCCCC|CCCC")

    original_len = sum(len(line) for line in lines)
    # Substitute sub-strings: VIIII->IX, IIII->IV, LXXXX->XC, XXXX->XL, DCCCC->CM, CCCC->CD
    # Notice that substituting with "XX" preserves length savings identical to 2-character subtractive pairs!
    minimal_len = sum(len(pattern.sub("XX", line)) for line in lines)

    # Return total characters saved
    return original_len - minimal_len


if __name__ == "__main__":
    print(solve())
