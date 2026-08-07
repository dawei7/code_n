## General
Given an integer `n`. Consider an equilateral triangle of side length `n`, broken up into $n^{2}$ unit equilateral triangles. The triangle has `n` **1-indexed** rows where the $$i^{\text{th}}$$ row has $2i - 1$ unit equilat..., the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n^2)$ — Auxiliary memory allocation bound.
