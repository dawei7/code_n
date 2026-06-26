"""Optimal solution for recursion_03: Print Subsequences.

For each position, branch on include/exclude. The recursion
tree has 2^n leaves; each leaf is a distinct subsequence.
Sorted so the verify can do a plain equality check.
"""


def solve(s, n):
    result = []

    def helper(i, path):
        if i == n:
            result.append("".join(path))
            return
        # Exclude s[i].
        helper(i + 1, path)
        # Include s[i].
        path.append(s[i])
        helper(i + 1, path)
        path.pop()

    helper(0, [])
    result.sort()
    return result
