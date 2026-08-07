## General
Given There exists an infinite number line, with its origin at 0 and extending towards the **positive** x-axis, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(q log C)$ — Operation count bound.
- **Space Complexity**: $O(C)$ — Auxiliary memory allocation bound.
