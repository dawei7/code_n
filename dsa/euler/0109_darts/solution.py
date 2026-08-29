def solve(max_score: int = 100) -> int:
    """Find the number of distinct checkout combinations with total score < max_score (100).

    Mathematical Principles Applied:
    1. Darts Checkout Structure:
       A checkout consists of up to 3 darts, where the LAST dart MUST be a Double (D1..D20 or D25).
       The first two darts can be any valid dart regions (Miss = 0, S1..S20, D1..D20, T1..T20, S25, D25)
       or a Miss (0 points).

    2. Unordered First Two Darts Symmetry:
       The order of the first two darts does NOT matter (e.g. S1 + S2 + D1 is identical to S2 + S1 + D1).
       Therefore, we iterate pairs (d1, d2) with index i <= j across the 63 possible first/second dart regions.

    3. Total Checkout Count:
       Sum over (i <= j) and final double d3 where val(d1) + val(d2) + val(d3) < 100.

    Time Complexity: O(63^2 * 21) = 43,659 checks (executes in ~0.01s).
    Space Complexity: O(1) constant auxiliary space.
    """
    # 1. Normal Darts (Miss + Singles + Doubles + Trebles)
    normal_darts = [(0, "M")]  # Miss (0 points)

    for i in range(1, 21):
        normal_darts.append((i, f"S{i}"))
        normal_darts.append((2 * i, f"D{i}"))
        normal_darts.append((3 * i, f"T{i}"))
    normal_darts.append((25, "S25"))
    normal_darts.append((50, "D25"))

    # Sort normal darts list
    normal_darts.sort()

    # 2. Doubles for Final Checkout Dart
    doubles = [(2 * i, f"D{i}") for i in range(1, 21)] + [(50, "D25")]

    checkout_count = 0

    # Iterate unordered pairs of first two darts (index i <= j)
    for i in range(len(normal_darts)):
        val1 = normal_darts[i][0]
        for j in range(i, len(normal_darts)):
            val2 = normal_darts[j][0]
            # Final dart MUST be a double
            for val_d, _ in doubles:
                total = val1 + val2 + val_d
                # Count checkout if total score is strictly less than 100
                if total < max_score:
                    checkout_count += 1

    # Return total count of distinct checkout combinations < 100
    return checkout_count


if __name__ == "__main__":
    print(solve())
