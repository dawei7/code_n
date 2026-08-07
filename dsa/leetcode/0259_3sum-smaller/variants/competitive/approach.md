## General
Given an array of `n` integers `nums` and an integer `target`, find the number of index triplets `i`, `j`, `k` with $0 \le i < j < k < n$ that satisfy the condition $\text{nums}[i] + \text{nums}[j] + \text{nums}[k] < target$, the algorithm solves **3Sum Smaller** directly. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
