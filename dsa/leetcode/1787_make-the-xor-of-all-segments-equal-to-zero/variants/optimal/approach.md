## General
Given an array `nums`​​​ and an integer `k`​​​​​. The XOR of a segment `[left, right]` where $left \le right$ is the `XOR` of all the elements with indices between `left` and `right`, inclusive: $\text{nums}[left] XOR nums[..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nX)$ — Operation count bound.
- **Space Complexity**: $O(X)$ — Auxiliary memory allocation bound.
