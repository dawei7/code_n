## General
Given There is an infrastructure of `n` cities with some number of `roads` connecting these cities. Each $\text{roads}[i] = [a_{i}, b_{i}]$ indicates that there is a bidirectional road between cities $a_{i}$ and $b_{i}$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n^2+m)$ — Operation count bound.
- **Space Complexity**: $O(n^2)$ — Auxiliary memory allocation bound.
