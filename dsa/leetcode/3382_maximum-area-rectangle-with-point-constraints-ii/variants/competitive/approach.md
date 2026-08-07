## General
Given There are n points on an infinite plane. You are given two integer arrays `xCoord` and `yCoord` where $(\text{xCoord}[i], \text{yCoord}[i])$ represents the coordinates of the $$i^{\text{th}}$$ point, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
