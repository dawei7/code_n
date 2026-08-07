## General
Given Consider a matrix `M` with dimensions $width * height$, such that every cell has value `0` or `1`, and any **square** sub-matrix of `M` of size $sideLength * sideLength$ has at most `maxOnes` ones, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(s^2\log s)$ — Operation count bound.
- **Space Complexity**: $O(s^2)$ — Auxiliary memory allocation bound.
