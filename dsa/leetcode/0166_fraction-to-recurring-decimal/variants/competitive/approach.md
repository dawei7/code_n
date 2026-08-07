## General
Given two integers representing the `numerator` and `denominator` of a fraction, return *the fraction in string format*, the algorithm solves **Fraction to Recurring Decimal** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(k)$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
