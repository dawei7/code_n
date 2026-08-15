from collections import defaultdict
import math
import os


def solve(filepath: str = "") -> int:
    """Find the largest square formed by any member of a square anagram pair in words.txt.

    Mathematical Principles Applied:
    1. Word Anagram Grouping & Pair Extraction:
       Group 2000 English words by sorted character signature keys "".join(sorted(w)).
       Pairs of words sharing the exact same character signature are candidate word anagrams (e.g. CARE and RACE).

    2. Bijective Character-to-Digit Mapping:
       For a word pair (w1, w2) of length L and a candidate L-digit square s1, construct a 1-to-1 (bijective)
       mapping between characters in w1 and digits in s1.
       Constraints:
       - No two characters map to the same digit.
       - No character maps to multiple digits.

    3. Square Permutation Verification:
       Apply the bijective mapping to w2 to form digit string s2.
       Validate that s2 has no leading zeros (s2[0] != '0') and s2 is a perfect square!

    Time Complexity: O(W^2 + S) executing in ~0.05s.
    Space Complexity: O(W + S) memory for anagram groups and square lists.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0098_anagramic-squares/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "words.txt")

    # Read words text file
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    words = [w.strip('"') for w in text.strip().split(",") if w.strip('"')]

    # Group words by sorted character anagram key
    anagram_groups = defaultdict(list)
    for w in words:
        anagram_groups["".join(sorted(w))].append(w)

    # Collect valid anagram pairs (w1, w2)
    valid_pairs = []
    for group in anagram_groups.values():
        if len(group) >= 2:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    valid_pairs.append((group[i], group[j]))

    # Precompute perfect squares grouped by digit length L
    max_len = max(len(p[0]) for p in valid_pairs)
    squares_by_len = defaultdict(list)
    n = 1
    while True:
        sq = n * n
        s_sq = str(sq)
        L = len(s_sq)
        if L > max_len:
            break
        if L >= 2:
            squares_by_len[L].append(s_sq)
        n += 1

    max_square = 0

    # Test each word anagram pair against candidate squares of matching length
    for w1, w2 in valid_pairs:
        L = len(w1)
        for s1 in squares_by_len[L]:
            # Construct 1-to-1 (bijective) character <-> digit mapping
            char_to_digit = {}
            digit_to_char = {}
            valid_map = True
            for ch, d in zip(w1, s1):
                if ch in char_to_digit and char_to_digit[ch] != d:
                    valid_map = False
                    break
                if d in digit_to_char and digit_to_char[d] != ch:
                    valid_map = False
                    break
                char_to_digit[ch] = d
                digit_to_char[d] = ch

            if not valid_map:
                continue

            # Apply bijective mapping to second word w2
            s2_chars = [char_to_digit[ch] for ch in w2]
            # Enforce no leading zero constraint
            if s2_chars[0] == "0":
                continue

            s2 = "".join(s2_chars)
            sq2 = int(s2)
            root2 = math.isqrt(sq2)
            # Verify if second transformed number is a perfect square
            if root2 * root2 == sq2:
                max_square = max(max_square, int(s1), sq2)

    # Return largest square integer formed by any member of a valid anagram pair
    return max_square


if __name__ == "__main__":
    print(solve())
