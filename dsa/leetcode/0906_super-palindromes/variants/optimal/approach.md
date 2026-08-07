## General
Given Let's say a positive integer is a **super-palindrome** if it is a palindrome, and it is also the square of a palindrome, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(\sqrt{m}\log R)$ — Operation count bound.
- **Space Complexity**: $O(\log R)$ — Auxiliary memory allocation bound.
