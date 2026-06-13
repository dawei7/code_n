"""Optimal solution for hash_04: Group Anagrams.

Two strings are anagrams iff their sorted characters are equal.
Use a dict keyed on the sorted-tuple; collect the original
strings into per-key lists. Sort each group's inner list and
the outer list of group keys so the verify can compare
directly. O(n * k log k) where k is the string length.
"""


def solve(strs, n):
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        groups.setdefault(key, []).append(s)
    out = []
    for key in groups:
        out.append(sorted(groups[key]))
    out.sort(key=lambda g: g[0])
    return out
