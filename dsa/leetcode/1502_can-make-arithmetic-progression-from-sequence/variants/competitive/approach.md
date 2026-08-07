## General
Given A sequence of numbers is called an **arithmetic progression** if the difference between any two consecutive elements is the same, the algorithm solves **Can Make Arithmetic Progression From Sequence** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
