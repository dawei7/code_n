"""Optimal solution for approx_02: Set Cover (Greedy).

Each step picks the set covering the most uncovered elements.
"""


def solve(universe, sets, m, k):
    if k == 0:
        return []
    uncovered = set(universe)
    chosen = []
    while uncovered:
        best_idx = -1
        best_count = 0
        for i, s in enumerate(sets):
            count = sum(1 for x in s if x in uncovered)
            if count > best_count:
                best_count = count
                best_idx = i
        if best_idx == -1 or best_count == 0:
            break
        chosen.append(best_idx)
        for x in sets[best_idx]:
            uncovered.discard(x)
    return sorted(chosen)
