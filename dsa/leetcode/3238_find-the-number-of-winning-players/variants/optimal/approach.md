## General
Given an integer `n` representing the number of players in a game and a 2D array `pick` where $\text{pick}[i] = [x_{i}, y_{i}]$ represents that the player $x_{i}$ picked a ball of color $y_{i}$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(p)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
