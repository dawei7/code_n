## General
Given a string `road`, consisting only of characters `"x"` and `"."`, where each `"x"` denotes a *pothole* and each `"."` denotes a smooth road, and an integer `budget`, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n + r log r)$ — Operation count bound.
- **Space Complexity**: $O(r)$ — Auxiliary memory allocation bound.
