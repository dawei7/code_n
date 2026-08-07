## General
Given two strings low and high that represent two integers `low` and `high` where $low \le high$, return *the number of **strobogrammatic numbers** in the range* `[low, high]`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(d \cdot 5^{d/2})$ — Operation count bound.
- **Space Complexity**: $O(d)$ — Auxiliary memory allocation bound.
