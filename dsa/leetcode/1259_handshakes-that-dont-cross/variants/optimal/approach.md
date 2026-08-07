## General
Given an **even** number of people `numPeople` that stand around a circle and each person shakes hands with someone else so that there are $numPeople / 2$ handshakes total, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(p+\log M)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
