def solve(max_score: int = 100) -> int:
    """Find number of distinct checkout combinations with total score < max_score.
    
    Time Complexity: O(N^2 * D)
    Space Complexity: O(1)
    """
    # 1. Normal Darts (Miss + Singles + Doubles + Trebles)
    normal_darts = [(0, 'M')]  # Miss (0 points)

    for i in range(1, 21):
        normal_darts.append((i, f"S{i}"))
        normal_darts.append((2 * i, f"D{i}"))
        normal_darts.append((3 * i, f"T{i}"))
    normal_darts.append((25, "S25"))
    normal_darts.append((50, "D25"))

    # Assign integer ID for canonical unordered pair indexing
    normal_darts.sort()

    # 2. Doubles for Final Dart
    doubles = [(2 * i, f"D{i}") for i in range(1, 21)] + [(50, "D25")]

    checkout_count = 0

    # Iterate unordered pairs of first two darts (d1 <= d2)
    for i in range(len(normal_darts)):
        val1 = normal_darts[i][0]
        for j in range(i, len(normal_darts)):
            val2 = normal_darts[j][0]
            # Final dart must be a double
            for val_d, _ in doubles:
                total = val1 + val2 + val_d
                if total < max_score:
                    checkout_count += 1

    return checkout_count
