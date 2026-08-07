## General
Given a 2D integer array `circles` where $\text{circles}[i] = [x_{i}, y_{i}, r_{i}]$ represents the center $(x_{i}, y_{i})$ and radius $r_{i}$ of the $$i^{\text{th}}$$ circle drawn on a grid, return *the **number of lattice..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(sum r_i^2)$ — Operation count bound.
- **Space Complexity**: $O(P)$ — Auxiliary memory allocation bound.
