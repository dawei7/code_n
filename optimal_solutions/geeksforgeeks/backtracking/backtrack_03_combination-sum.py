"""Optimal solution for backtrack_03: Combination Sum.

Given a list of positive integers and a target, return every
unique combination that sums to target. Each input element may
be used any number of times. Sort the input first and always
recurse forward (i >= start) to avoid duplicates.
"""


def solve(candidates, target, n):
    candidates = sorted(candidates)
    result = []

    def helper(start, remaining, path):
        if remaining == 0:
            result.append(list(path))
            return
        if start == n or remaining < 0:
            return
        for i in range(start, n):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            helper(i, remaining - candidates[i], path)
            path.pop()

    helper(0, target, [])
    return result
