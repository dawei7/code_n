## General
Given A perfectly straight street is represented by a number line. The street has building(s) on it and is represented by a 2D integer array `buildings`, where $\text{buildings}[i] = [\text{start}_{i}, \text{end}_{i}, \text..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(B\log B)$ — Operation count bound.
- **Space Complexity**: $O(B)$ — Auxiliary memory allocation bound.
