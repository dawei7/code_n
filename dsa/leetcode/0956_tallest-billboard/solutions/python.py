"""Optimal app-local solution for LeetCode 956."""


def solve(rods):
    best_shorter = {0: 0}
    for rod in rods:
        updated = dict(best_shorter)
        for difference, shorter in best_shorter.items():
            taller_difference = difference + rod
            updated[taller_difference] = max(updated.get(taller_difference, -1), shorter)

            balanced_difference = abs(difference - rod)
            balanced_shorter = shorter + min(difference, rod)
            updated[balanced_difference] = max(
                updated.get(balanced_difference, -1), balanced_shorter
            )
        best_shorter = updated
    return best_shorter[0]
