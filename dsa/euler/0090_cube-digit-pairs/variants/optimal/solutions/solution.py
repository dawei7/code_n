import itertools


def solve() -> int:
    """Find number of distinct arrangements of two 6-faced cubes that display all 2-digit squares below 100.
    
    Time Complexity: O(C(10, 6)^2)
    Space Complexity: O(1)
    """
    squares = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]

    combinations = list(itertools.combinations(range(10), 6))
    valid_count = 0

    for i in range(len(combinations)):
        c1 = set(combinations[i])
        if 6 in c1 or 9 in c1:
            c1.add(6)
            c1.add(9)

        for j in range(i, len(combinations)):
            c2 = set(combinations[j])
            if 6 in c2 or 9 in c2:
                c2.add(6)
                c2.add(9)

            possible = True
            for d1, d2 in squares:
                if not ((d1 in c1 and d2 in c2) or (d2 in c1 and d1 in c2)):
                    possible = False
                    break

            if possible:
                valid_count += 1

    return valid_count
