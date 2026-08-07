## General
Given an integer array `nums`, return `0`* if the sum of the digits of the minimum integer in *`nums`* is odd, or *`1`* otherwise*, the algorithm solves **Sum of Digits in the Minimum Number** directly. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n+D)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
