## General
Given Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((h + t) \log(h + t))$ — Operation count bound.
- **Space Complexity**: $O(t)$ — Auxiliary memory allocation bound.
