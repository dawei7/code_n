## General
Given You have an `inventory` of different colored balls, and there is a customer that wants `orders` balls of **any** color, the algorithm solves **Sell Diminishing-Valued Colored Balls** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n\log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
