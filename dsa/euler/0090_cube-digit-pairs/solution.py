import itertools


def solve() -> int:
    """Find the number of distinct arrangements of two 6-faced cubes that can display all 2-digit squares below 100.

    Mathematical Principles Applied:
    1. Combination Space for 6-Faced Cubes:
       Choosing 6 distinct digits from 10 digits {0..9} gives C(10, 6) = 210 possible cube face sets.

    2. Reversible 6/9 Equivalence:
       If 6 or 9 is present on a cube, the die can be inverted to display both 6 and 9.
       Therefore, if 6 or 9 is in a face set, we add BOTH 6 and 9 to the expanded digit set.

    3. 2-Digit Square Display Condition:
       The 9 2-digit square numbers below 100 are:
       01, 04, 09, 16, 25, 36, 49, 64, 81.
       For each square (d1, d2), either (d1 in C1 and d2 in C2) or (d2 in C1 and d1 in C2) must hold.

    Time Complexity: O(C(10, 6)^2) over 210 * 211 / 2 = 22,155 pairs (executes in ~0.02s).
    Space Complexity: O(1) constant auxiliary space.
    """
    # 2-digit squares below 100: 01, 04, 09, 16, 25, 36, 49, 64, 81
    squares = [
        (0, 1),
        (0, 4),
        (0, 9),
        (1, 6),
        (2, 5),
        (3, 6),
        (4, 9),
        (6, 4),
        (8, 1),
    ]

    # Generate all C(10, 6) = 210 6-digit combinations
    combinations = list(itertools.combinations(range(10), 6))
    valid_count = 0

    # Iterate distinct pairs of cube face combinations (i <= j)
    for i in range(len(combinations)):
        c1 = set(combinations[i])
        # Reversible 6/9 rule for cube 1
        if 6 in c1 or 9 in c1:
            c1.add(6)
            c1.add(9)

        for j in range(i, len(combinations)):
            c2 = set(combinations[j])
            # Reversible 6/9 rule for cube 2
            if 6 in c2 or 9 in c2:
                c2.add(6)
                c2.add(9)

            # Check if all 9 squares can be formed by (c1, c2)
            possible = True
            for d1, d2 in squares:
                if not ((d1 in c1 and d2 in c2) or (d2 in c1 and d1 in c2)):
                    possible = False
                    break

            # Increment valid arrangement counter
            if possible:
                valid_count += 1

    # Return total count of distinct valid 2-cube arrangements
    return valid_count


if __name__ == "__main__":
    print(solve())
