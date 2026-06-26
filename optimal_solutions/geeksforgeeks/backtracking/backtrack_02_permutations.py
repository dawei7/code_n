"""Optimal solution for backtrack_02: Permutations.

Return every ordering of ``arr`` as a list of lists. Standard
backtracking: pick each unused element in turn, recurse, then
unpick. The output list of permutations is sorted so the
verify can do a plain equality check.
"""


def solve(arr, n):
    if n == 0:
        return [[]]
    result = []
    used = [False] * n

    def helper(path):
        if len(path) == n:
            result.append(list(path))
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(arr[i])
                helper(path)
                path.pop()
                used[i] = False

    helper([])
    result.sort()
    return result
