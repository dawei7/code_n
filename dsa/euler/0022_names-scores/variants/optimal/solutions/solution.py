import os


def solve(filepath: str = "") -> int:
    """Find total of all name scores in the names file.

    Mathematical Principles Applied:
    1. Lexicographical Sorting:
       Sort N = 5,163 names in alphabetical order: S_1 < S_2 < ... < S_N.

    2. Alphabetical Character Sum V(S):
       For a name S, V(S) = sum_{c in S} (ord(c) - 64).

    3. Indexed Name Score Product:
       Name score for S_k at position k (1-indexed) is k * V(S_k).
       Total score = sum_{k=1}^N k * V(S_k).

    Time Complexity: O(N log N * L) for sorting where N = 5163 and L ≈ 6.
    Space Complexity: O(N * L) memory to store name list.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach problem package root (0022_names-scores/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "names.txt")

    # Read names text file
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse and lexicographically sort names list
    names = sorted([w.strip('"') for w in content.strip().split(",") if w.strip()])

    # Accumulate name scores: 1-indexed position k multiplied by letter value sum
    total_score = 0
    for idx, name in enumerate(names, 1):
        letter_val = sum(ord(c) - 64 for c in name.upper() if "A" <= c <= "Z")
        total_score += idx * letter_val

    # Return total sum of all name scores
    return total_score


if __name__ == "__main__":
    print(solve())
