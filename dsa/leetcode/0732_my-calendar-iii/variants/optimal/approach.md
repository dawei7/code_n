## General
Given A `k`-booking happens when `k` events have some non-empty intersection (i.e., there is some time that is common to all `k` events.), the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(q \log C)$ — Operation count bound.
- **Space Complexity**: $O(q \log C)$ — Auxiliary memory allocation bound.
