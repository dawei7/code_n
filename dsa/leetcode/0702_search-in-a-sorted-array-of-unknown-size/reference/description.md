## Description

This is an interactive problem. A secret array contains unique integers in strictly increasing order, but its length is unknown and the array cannot be accessed directly. Instead, `ArrayReader.get(i)` returns `secret[i]` for a valid zero-based index `i`, or the sentinel $2^{31} - 1$ when `i` is outside the array boundary.

Given an integer `target`, return the index `k` for which `secret[k] == target`. Return `-1` when the target is absent. The algorithm must run in $O(\log n)$ time even though the array size is unavailable.
