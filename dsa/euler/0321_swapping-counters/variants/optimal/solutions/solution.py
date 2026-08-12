def solve(count: int = 40) -> int:
    """Find the sum of the first 40 terms of n for which M(n) is a triangle number.
    
    Time Complexity: O(count) via Generalized Pell Equation Recurrence
    Space Complexity: O(count)
    """
    fam1 = (1, 2)
    fam2 = (5, 4)

    terms = []
    x1, y1 = fam1
    x2, y2 = fam2

    for _ in range(count):
        if y1 > 2 and (y1 - 2) % 2 == 0:
            terms.append((y1 - 2) // 2)
        if y2 > 2 and (y2 - 2) % 2 == 0:
            terms.append((y2 - 2) // 2)

        x1, y1 = 3 * x1 + 4 * y1, 2 * x1 + 3 * y1
        x2, y2 = 3 * x2 + 4 * y2, 2 * x2 + 3 * y2

    terms.sort()
    return sum(terms[:count])
