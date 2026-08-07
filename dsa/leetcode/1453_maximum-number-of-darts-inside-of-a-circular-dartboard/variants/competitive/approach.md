## General
Given Alice is throwing `n` darts on a very large wall. You are given an array `darts` where $\text{darts}[i] = [x_{i}, y_{i}]$ is the position of the $$i^{\text{th}}$$ dart that Alice threw on the wall, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n^2\log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
