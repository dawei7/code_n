## General
Given a **0-indexed** 2D integer array `nums` representing the coordinates of the cars parking on a number line. For any index `i`, $\text{nums}[i] = [\text{start}_{i}, \text{end}_{i}]$ where $\text{start}_{i}$ is the start..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
