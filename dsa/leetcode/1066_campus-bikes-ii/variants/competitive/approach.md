## General
Given On a campus represented as a 2D grid, there are `n` workers and `m` bikes, with $n \le m$. Each worker and bike is a 2D coordinate on this grid, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(B2^B)$ — Operation count bound.
- **Space Complexity**: $O(2^B)$ — Auxiliary memory allocation bound.
