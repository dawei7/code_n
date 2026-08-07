## General
Given an array `nums` of length `n`, return an array `answer` of length $n - 1$ such that $\text{answer}[i] = \text{nums}[i] | nums[i + 1]$ where `|` is the bitwise `OR` operation, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
