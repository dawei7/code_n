## General
Given a **2D** integer array `coordinates` and an integer `k`, where $\text{coordinates}[i] = [x_{i}, y_{i}]$ are the coordinates of the $$i^{\text{th}}$$ point in a 2D plane, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(nk)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
