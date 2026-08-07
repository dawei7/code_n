## General
Given `n` rectangles represented by a **0-indexed** 2D integer array `rectangles`, where $\text{rectangles}[i] = [\text{width}_{i}, \text{height}_{i}]$ denotes the width and height of the $$i^{\text{th}}$$ rectangle, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(N\log M)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
