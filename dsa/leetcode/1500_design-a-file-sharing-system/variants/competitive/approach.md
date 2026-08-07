## General
Given We will use a file-sharing system to share a very large file which consists of `m` small **chunks** with IDs from `1` to `m`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(k + \log U + p \log p)$ — Operation count bound.
- **Space Complexity**: $O(U + H)$ — Auxiliary memory allocation bound.
