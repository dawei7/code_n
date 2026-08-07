## General
Given There is a ball in a `maze` with empty spaces (represented as `0`) and walls (represented as `1`). The ball can go through the empty spaces by rolling **up, down, left or right**, but it won't stop rolling until hitti..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(rows \cdot cols \cdot p \log(rows \cdot cols))$ — Operation count bound.
- **Space Complexity**: $O(rows \cdot cols \cdot p)$ — Auxiliary memory allocation bound.
