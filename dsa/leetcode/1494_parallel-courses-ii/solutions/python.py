"""Optimal app-local solution for LeetCode 1494."""

from itertools import combinations


def solve(n: int, relations: list[list[int]], k: int) -> int:
    """Return the minimum semesters under prerequisites and a capacity limit."""
    if not relations:
        return (n + k - 1) // k

    prerequisites = [0] * n
    for previous, following in relations:
        prerequisites[following - 1] |= 1 << (previous - 1)

    full_mask = (1 << n) - 1
    unreachable = n + 1
    semesters = [unreachable] * (1 << n)
    semesters[0] = 0

    for done in range(full_mask):
        if semesters[done] == unreachable:
            continue

        available_bits = []
        for course in range(n):
            bit = 1 << course
            if done & bit == 0 and prerequisites[course] & done == prerequisites[course]:
                available_bits.append(bit)

        if len(available_bits) <= k:
            take = sum(available_bits)
            next_state = done | take
            semesters[next_state] = min(semesters[next_state], semesters[done] + 1)
            continue

        for chosen in combinations(available_bits, k):
            take = sum(chosen)
            next_state = done | take
            semesters[next_state] = min(semesters[next_state], semesters[done] + 1)

    return semesters[full_mask]

