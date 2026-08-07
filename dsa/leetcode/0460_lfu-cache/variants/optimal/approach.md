## General
Given Design and implement a data structure for a <a href="https://en.wikipedia.org/wiki/Least_frequently_used" target="_blank">Least Frequently Used (LFU)</a> cache, the algorithm solves **LFU Cache** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(m)$ — Operation count bound.
- **Space Complexity**: $O(capacity)$ — Auxiliary memory allocation bound.
