## General
Given a string `s`, find the length of the **longest** **substring** without duplicate characters, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(\min(n, a))$ — Auxiliary memory allocation bound.
