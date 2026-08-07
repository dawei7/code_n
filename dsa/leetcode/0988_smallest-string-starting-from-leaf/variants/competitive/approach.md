## General
Given the `root` of a binary tree where each node has a value in the range `[0, 25]` representing the letters `'a'` to `'z'`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(NH)$ — Operation count bound.
- **Space Complexity**: $O(H)$ — Auxiliary memory allocation bound.
