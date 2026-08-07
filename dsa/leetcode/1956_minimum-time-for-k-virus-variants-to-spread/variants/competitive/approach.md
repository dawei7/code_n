## General
Given There are `n` **unique** virus variants in an infinite 2D grid. You are given a 2D array `points`, where $\text{points}[i] = [x_{i}, y_{i}]$ represents a virus originating at $(x_{i}, y_{i})$ on day `0`. Note that it ..., the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(XYN\log N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
