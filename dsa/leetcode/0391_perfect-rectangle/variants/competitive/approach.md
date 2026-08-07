## General
Given an array `rectangles` where $\text{rectangles}[i] = [x_{i}, y_{i}, a_{i}, b_{i}]$ represents an axis-aligned rectangle. The bottom-left point of the rectangle is $(x_{i}, y_{i})$ and the top-right point of it is $(a_{..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(r)$ — Operation count bound.
- **Space Complexity**: $O(r)$ — Auxiliary memory allocation bound.
