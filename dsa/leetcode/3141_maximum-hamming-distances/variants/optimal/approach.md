## General
Given an array `nums` and an integer `m`, with each element $\text{nums}[i]$ satisfying $0 \le \text{nums}[i] < 2^m$, return an array `answer`. The `answer` array should be of the same length as `nums`, where each element $..., the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(m * 2^m + n)$ — Operation count bound.
- **Space Complexity**: $O(2^m)$ — Auxiliary memory allocation bound.
